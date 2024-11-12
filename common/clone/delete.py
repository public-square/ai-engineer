import os
from django.conf import settings
from common.utils import parse_repository_string

def delete_clone(repository):
    """
    Delete a local repository clone.

    Args:
        repository (str): Repository string in format 'owner/repo/branch' or 'owner/repo'
                         (branch defaults to 'main')

    Returns Either:
        On success:
            {
                'status': 'success',
                'repository': 'owner/repo/branch',
                'path': '/path/to/clone'
            }
        On error:
            {
                'error': '<error message>'
            }
    """
    try:
        owner, repo, branch = parse_repository_string(repository)
        clone_dir = f"{settings.GITHUB_CLONE_DIR}/{owner}/{repo}/{branch}"
        # delete the clone dir if it exists
        if os.path.exists(clone_dir):
            os.system(f'rm -rf {clone_dir}')
            return {
                'status': 'success',
                'repository': f'{owner}/{repo}/{branch}',
                'path': clone_dir
            }
        else:
            return {
                'error': f'Clone does not exist: {clone_dir}'
            }
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f'Failed to delete clone: {str(e)}'}
