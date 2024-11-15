"""
URL configuration for the AI Engineer API.

This module defines the URL patterns for the API endpoints:
- /api/ping/ (POST):
        Accepts text strings and returns both original and reversed versions
        Handles input validation and error responses
        Maximum text length: 1024 characters

- /api/llm/prompt/ (POST):
        Accepts text strings and returns llm responses
        Handles input validation and error responses
        Maximum text length: 1024 characters

- /api/ragindex/vectorize/ (POST):
        Vectorizes GitHub repository contents and stores them in Pinecone
        Accepts repository string in format 'owner/repo/branch' or 'owner/repo'
        where 'branch' is optional (defaults to 'main')
        The leading '/' is optional
        Examples:
            - 'microsoft/vscode'
            - '/microsoft/vscode'
            - 'microsoft/vscode/develop'
            - '/microsoft/vscode/main'
        Processes .md and .py files
        Returns success status and number of processed files
        Handles invalid inputs and processing errors

- /api/ragindex/list/ (GET):
        Lists all repositories (namespaces) stored in the Pinecone database
        Returns a sorted list of repositories in format 'owner/repo/branch'
        No input parameters required

- /api/ragindex/delete/ (DELETE):
        Deletes all vectors for a repository from the Pinecone database
        Accepts repository string in format 'owner/repo/branch' or 'owner/repo'
        where 'branch' is optional (defaults to 'main')
        The leading '/' is optional
        Returns success status on completion
        Returns 404 if repository not found
"""

from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('ragindex/vectorize/', views.ragindex.vectorize.vectorize_repository_view, name='vectorize_repository'),
    path('ragindex/list/', views.ragindex.list.list_repositories_view, name='list_repositories'),
    path('ragindex/delete/', views.ragindex.delete.delete_repository_view, name='delete_repository'),
    path('llm/prompt/', views.llm.prompt.chat_with_gpt_view, name='chat_with_gpt'),
    path('agent/analyze/codereview/', views.agent.analyze.analyze_code_review_view, name='analyze_code_review'),
]
