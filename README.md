# ai-engineer
Simple generative AI for software development. Manages local github repository
clones and Pinecone indexing for RAG.

Python 3.12 virtual execution environment and dependencies are managed via
Poetry. Installed dependencies include support for LangGraph, OpenAI, Github,
PineCone.

Multiple agents will be added soon.

## Setup
Python3.12 must be installed at the system level. All execution will use a
virtual environment.

### Configure System Poetry
```bash
python3.12 -m pip install poetry
python3.12 -m poetry config virtualenvs.in-project true
python3.12 -m poetry config virtualenvs.create true
```

### Local Virtual Execution Environment
Instantiate the virtual execution environment in the application root.
```bash
echo exit | python3.12 -m poetry shell
.venv/bin/python -m pip install poetry
.venv/bin/python -m poetry install
```

## Configuration
Copy `global/./env-sample` to `global/.env`.

Obtain keys and set `OPENAI_API_KEY`, `PINECONE_API_KEY`, and `LANGCHAIN_API_KEY`.

Create a Pincone index for RAG.

```bash
./ai-engineer setup-index
```

## Vectorize a Repository for RAG
Repositories for RAG are stored in individual namespaces. Add this one.

```bash
./ai-engineer repo-vectorize --repo public-square/ai-engineer/main
```

Pause while Pinecone makes the index available. Verify that it is ready:

```bash
./ai-engineer repo-list
```

## Verify RAG
LLM prompts with an indexed repository specified use that repository for RAG.
```bash
./ai-engineer chat \
--repo 'public-square/ai-engineer/main' \
--prompt "What is the curl command I should use to hit the ping API target?"
```

## Verify API
Launch the API server.

```bash
./ai-engineer-ctrl start
```

Check results.
```bash
curl --silent -X POST -H "Content-Type: application/json" \
http://localhost:8001/api/chat/prompt/ -d @- << EOF |
{
  "prompt": "What is the curl command I should use to hit the ping API target?",
  "repository": "public-square/ai-engineer/main"
}
EOF
jq
```

