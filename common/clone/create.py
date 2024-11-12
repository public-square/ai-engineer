import os
from django.conf import settings
from common.utils import parse_repository_string
import pygit2

def create_clone(repository):
    """
    Create a local clone of the specified repository at the specified branch.

    Args:
        repository (str): Repository string in format 'owner/repo/branch'
                        (branch is optional, defaults to 'main')

    Returns:
        dict: A dictionary containing:
            - On success:
                {
                    'status': 'success',
                    'owner': <owner>,
                    'repo': <repo>,
                    'branch': <branch>
                }
            - On error:
                {
                    'error': <error_message>
                }

    Raises:
        ValueError: If repository string is invalid
        Exception: If there's an error processing the repository
    """
    try:
        owner, repo, branch = parse_repository_string(repository)
        clone_dir = f"{settings.GITHUB_CLONE_DIR}/{owner}/{repo}/{branch}"
        repo_url = f"https://github.com/{owner}/{repo}.git"

        # make sure the full clone dir path exists
        os.makedirs(clone_dir, exist_ok=True)
        # delete the clone dir if it exists
        if os.path.exists(clone_dir):
            os.system(f'rm -rf {clone_dir}')

        # clone the repo at the specified branch
        pygit2.clone_repository(repo_url, clone_dir, checkout_branch=f"{branch}")
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

    return {
        'status': 'success',
        'owner': owner,
        'repo': repo,
        'branch': branch
    }
