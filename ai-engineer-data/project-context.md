# Project Context for `ai-engineer`

## Overview
The `ai-engineer` project is a generative AI application designed to assist software development by managing local GitHub repository clones and utilizing Pinecone for retrieval-augmented generation (RAG). The application is built using Python 3.12 and leverages various libraries and frameworks to provide its functionality.

## Major Libraries and Frameworks
- **Python**: `3.12`
- **Django**: `5.1.2`
- **Django REST Framework**: `3.15.2`
- **Poetry**: `1.8.4` (for dependency management)
- **aiohttp**: `3.9.5` (for asynchronous HTTP client/server)
- **aiohappyeyeballs**: `2.4.3` (for happy eyeballs in asyncio)
- **LangChain**: `0.3.7` (for language model integration)
- **OpenAI**: `1.52` (for OpenAI API integration)
- **Pinecone**: `5.3.1` (for vector storage and retrieval)
- **GitHub API Wrapper**: (custom library from GitHub)
- **pygit2**: `1.16.0` (for Git operations)

## Project Structure
### 1. **Root Files**
- **`README.md`**: Provides an overview of the project, setup instructions, and usage examples.
- **`pyproject.toml`**: Defines project metadata and dependencies managed by Poetry.
- **`poetry.lock`**: Automatically generated file that locks the versions of dependencies.

### 2. **Django Configuration**
- **`manage.py`**: Command-line utility for administrative tasks in Django.
- **`global/settings.py`**: Configuration settings for the Django application, including database settings, installed apps, and middleware.
- **`global/urls.py`**: URL routing for the Django application, linking to API endpoints.
- **`global/asgi.py`**: ASGI configuration for asynchronous support.
- **`global/wsgi.py`**: WSGI configuration for traditional web server support.

### 3. **API Endpoints**
- **`api/urls.py`**: Defines the URL patterns for the API endpoints.
- **`api/views/`**: Contains view functions for handling API requests, including:
  - **`ping.py`**: Endpoint for reversing a string.
  - **`ragindex/`**: Endpoints for managing RAG repositories (vectorization, listing, deletion).
  - **`llm/`**: Endpoint for interacting with the OpenAI language model.

### 4. **Common Utilities**
- **`common/utils.py`**: Contains utility functions for interacting with GitHub and processing file contents.
- **`common/ragindex/`**: Functions for managing RAG operations, including vectorization and deletion of repositories.
- **`common/clone/`**: Functions for managing local repository clones (creation, deletion, listing).

### 5. **Agent Functionality**
- **`common/agent/`**: Contains logic for analyzing code and providing project context or code reviews using agents.
- **`common/agent/analyze.py`**: Core logic for agent analysis, including code review and project context generation.

### 6. **Control Script**
- **`ai-engineer-ctrl`**: Bash script for controlling the API server (start, stop, status, listeners).

### 7. **Documentation**
- **`docs/`**: Contains various markdown files documenting the API, CLI usage, and Python execution environment.

## Key Functionalities
- **API Server**: Provides endpoints for string manipulation, repository management, and interaction with language models.
- **RAG Management**: Allows vectorization of GitHub repositories for enhanced AI responses.
- **Local Clone Management**: Facilitates the creation and management of local clones of GitHub repositories.
- **Agent Analysis**: Implements agents that can perform tasks such as code reviews and project context generation.

## Notes for Developers
- Familiarize yourself with the Django framework and REST API development.
- Understand the usage of Pinecone for vector storage and retrieval.
- Review the integration of OpenAI's API for language model interactions.
- Explore the structure of the project, especially the organization of views and utility functions.
- Pay attention to the command-line interface and control scripts for server management.

## Conclusion
The `ai-engineer` project is a comprehensive application that combines various technologies to enhance software development through AI. Understanding the project structure, key functionalities, and dependencies will be crucial for any developer looking to contribute to this codebase. 

---

If you have any critiques or suggestions for improvement, please let me know, and I will revise the project context accordingly!
