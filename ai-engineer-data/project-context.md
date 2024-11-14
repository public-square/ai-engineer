# Project Context for `ai-engineer`

## Overview
The `ai-engineer` project is a generative AI application designed to manage local GitHub repository clones and facilitate retrieval-augmented generation (RAG) using Pinecone for indexing. The application is built using Python 3.12 and utilizes the Django framework for its API. It integrates various libraries to enhance its capabilities, including OpenAI for language processing and LangChain for managing interactions with language models.

## Directory Structure
```
ai-engineer/
├── api/
│   ├── __init__.py
│   ├── tests.py
│   ├── urls.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── ping.py
│   │   ├── ragindex/
│   │   │   ├── __init__.py
│   │   │   ├── delete.py
│   │   │   ├── list.py
│   │   │   └── vectorize.py
│   │   └── llm/
│   │       ├── __init__.py
│   │       └── prompt.py
├── common/
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   ├── analyze_codereview_prompts.py
│   │   └── analyze_projectcontext_prompts.py
│   ├── clone/
│   │   ├── __init__.py
│   │   ├── create.py
│   │   ├── delete.py
│   │   ├── files.py
│   │   ├── list.py
│   │   └── write_file.py
│   ├── ragindex/
│   │   ├── __init__.py
│   │   ├── delete.py
│   │   ├── list.py
│   │   └── vectorize.py
│   ├── llm/
│   │   ├── __init__.py
│   │   └── prompt.py
│   └── utils.py
├── global/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── .env
├── manage.py
├── poetry.lock
└── pyproject.toml
```

## Major Libraries and Frameworks
- **Django**: ^5.1.2
- **Django REST Framework**: ^3.15.2
- **Poetry**: 1.8.4
- **aiohttp**: ^3.9.5
- **aiohappyeyeballs**: 2.4.3
- **LangChain**: ^0.3.7
- **Pinecone**: 5.3.1
- **OpenAI**: 1.52
- **Pygit2**: ^1.16.0

## Key Files and Their Responsibilities

### `README.md`
- Provides an overview of the project, including its purpose and functionality.
- Contains instructions for setting up the environment and configuring the application.

### `pyproject.toml`
- Defines the project metadata, dependencies, and build system.
- Specifies the Python version compatibility and the libraries used in the project.

### `poetry.lock`
- Automatically generated file that locks the versions of dependencies used in the project.

### `manage.py`
- Django's command-line utility for administrative tasks.
- Sets up the Django environment and executes commands.

### `ai-engineer` (CLI)
- Command-line interface for interacting with the application.
- Handles various commands related to repository management, RAG indexing, and agent invocation.

### `ai-engineer-ctrl` (Control Script)
- Bash script for managing the API server.
- Supports starting, stopping, and checking the status of the server.

### `api/urls.py`
- Defines the URL patterns for the API endpoints.
- Maps incoming requests to the appropriate view functions.

### `api/views/`
- Contains view functions that handle API requests and responses.
- Implements functionality for pinging, RAG indexing, and interacting with the LLM.

### `common/`
- Contains utility functions and modules for various functionalities, including repository management, file processing, and LLM interactions.

### `global/settings.py`
- Configuration settings for the Django application.
- Includes database settings, installed apps, middleware, and environment variable management.

## Important Functionalities
- **API Endpoints**: The application exposes several API endpoints for interacting with the AI functionalities, including:
  - `/api/ping/`: Reverses a provided text string.
  - `/api/ragindex/vectorize/`: Vectorizes GitHub repository contents and stores them in Pinecone.
  - `/api/ragindex/list/`: Lists all repositories stored in the Pinecone database.
  - `/api/ragindex/delete/`: Deletes vectors for a specified repository from Pinecone.
  - `/api/llm/prompt/`: Interacts with OpenAI's GPT model for generating responses.

- **Command Line Interface**: The `ai-engineer` CLI allows users to manage local repository clones, vectorize repositories for RAG, and invoke agents for tasks like code reviews and project context analysis.

- **Agent Functionality**: The application supports multiple agents that can perform tasks such as code reviews and project context analysis based on the indexed repositories.

## Notes
- Ensure that the environment variables are properly set in the `.env` file for API keys and other configurations.
- The application is designed to run in a virtual environment managed by Poetry to avoid dependency conflicts.
- The project is structured to facilitate easy extension and addition of new features, particularly in the agent functionalities.

## Conclusion
The `ai-engineer` project is a sophisticated application that leverages modern AI capabilities to enhance software development workflows. Understanding the structure, dependencies, and functionalities outlined above will be crucial for developers looking to contribute to or extend the project.
