import os
from django.conf import settings
from common.utils import parse_repository_string
from common.clone.files import formatted_files_from_clone


from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, AIMessage, ChatMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from tavily import TavilyClient

from .analyze_codereview_prompts import TASK_PROMPT, PLAN_PROMPT, RESEARCH_PLAN_PROMPT, WRITER_PROMPT, REFLECTION_PROMPT, RESEARCH_CRITIQUE_PROMPT





def agent_analyze(repository):
    try:
        owner, repo, branch = parse_repository_string(repository)
        clone_dir = f"{settings.GITHUB_CLONE_DIR}/{owner}/{repo}/{branch}"
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f'{str(e)}'}

    try:
        file_contents = formatted_files_from_clone(repository)
    except Exception as e:
        return {'error': f'Failed to read files: {str(e)}'}
    except ValueError as e:
        return {'error': str(e)}


    model = ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model="gpt-4o-mini",
        temperature=0
    )
    tavily = TavilyClient(
        api_key=settings.TAVILY_API_KEY
    )
    memory = MemorySaver()

    class AgentState(TypedDict):
        task: str
        plan: str
        draft: str
        critique: str
        content: List[str]
        revision_number: int
        max_revisions: int

    class Queries(BaseModel):
        queries: List[str]

    def plan_node(state: AgentState):
        messages = [
            SystemMessage(content=PLAN_PROMPT),
            HumanMessage(content=state['task'])
        ]
        response = model.invoke(messages)
        return {"plan": response.content}

    def research_plan_node(state: AgentState):
        queries = model.with_structured_output(Queries).invoke([
            SystemMessage(content=RESEARCH_PLAN_PROMPT),
            HumanMessage(content=state['task'])
        ])
        try:
            content = state['content']
        except KeyError:
            content = []
        for q in queries.queries:
            response = tavily.search(query=q, max_results=2)
            for r in response['results']:
                content.append(r['content'])
        return {"content": content}

    def generation_node(state: AgentState):
        content = "\n\n".join(state['content'] or [])
        user_message = HumanMessage(
            content=f"{state['task']}\n\nHere is my plan:\n\n{state['plan']}")
        messages = [
            SystemMessage(
                content=WRITER_PROMPT.format(content=content)
            ),
            user_message
            ]
        response = model.invoke(messages)
        return {
            "draft": response.content,
            "revision_number": state.get("revision_number", 1) + 1
        }

    def reflection_node(state: AgentState):
        messages = [
            SystemMessage(content=REFLECTION_PROMPT),
            HumanMessage(content=state['draft'])
        ]
        response = model.invoke(messages)
        return {"critique": response.content}

    def research_critique_node(state: AgentState):
        queries = model.with_structured_output(Queries).invoke([
            SystemMessage(content=RESEARCH_CRITIQUE_PROMPT),
            HumanMessage(content=state['critique'])
        ])
        content = state['content'] or []
        for q in queries.queries:
            response = tavily.search(query=q, max_results=2)
            for r in response['results']:
                content.append(r['content'])
        return {"content": content}

    def should_continue(state):
        if state["revision_number"] > state["max_revisions"]:
            return END
        return "reflect"



    builder = StateGraph(AgentState)
    builder.add_node("planner", plan_node)
    builder.add_node("generate", generation_node)
    builder.add_node("reflect", reflection_node)
    builder.add_node("research_plan", research_plan_node)
    builder.add_node("research_critique", research_critique_node)
    builder.set_entry_point("planner")
    builder.add_conditional_edges(
        "generate",
        should_continue,
        {END: END, "reflect": "reflect"}
    )


    builder.add_edge("planner", "research_plan")
    builder.add_edge("research_plan", "generate")
    builder.add_edge("reflect", "research_critique")
    builder.add_edge("research_critique", "generate")
    graph = builder.compile(checkpointer=memory)

    thread = {"configurable": {"thread_id": "1"}}
    for s in graph.stream({
        'task': TASK_PROMPT.format(file_contents=file_contents),
        "max_revisions": 2,
        "revision_number": 1,
    }, thread):
        if settings.DEBUG == "True":
            print(s, '\n\n')

    try:
        return {
            "status": "success",
            "codereview": s['generate']['draft']
        }
    except AttributeError as e:
        return {
            "status": "error",
            "error": f"Failed to generate code review: {str(e)}"
        }









