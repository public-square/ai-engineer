from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from common.agent.analyze import agent_analyze

@api_view(['POST'])
def analyze_code_review_view(request):
    """
    Analyze a local repository clone and return the code review.

    Accepts POST requests with a JSON body containing:
    {
        'repo': 'owner/repo/branch'  # branch is optional, defaults to 'main'
    }
    The repository string can optionally start with a forward slash.

    Examples:
        {
            'repo': 'microsoft/vscode'  # Uses 'main' branch
        }
        {
            'repo': 'microsoft/vscode/develop'  # Uses 'develop' branch
        }
        {
            'repo': '/microsoft/vscode/main'  # Leading slash is optional
        }

    Returns:
    200 OK: Successfully generated code review
    {
        'status': 'success',
        'content': 'Code review content here...'
    }

    400 Bad Request: Invalid input
    {
        'error': '<error message>'
    }

    500 Internal Server Error: Processing error
    {
        'error': '<error message>'
    }
    """
    if not request.data:
        return Response(
            {'error': 'Please provide repository string in the request body'},
            status=status.HTTP_400_BAD_REQUEST
        )

    repo = request.data.get('repo')
    if not repo:
        return Response(
            {'error': 'Repository parameter is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        analysis = agent_analyze('code_review', repo)

        if 'error' in analysis:
            return Response(
                {'error': analysis['error']},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if 'content' not in analysis:
            return Response(
                {'error': 'Analyze content not found'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({
            'status': 'success',
            'content': analysis['content']
        })

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

