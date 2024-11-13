import os
from django.conf import settings
from common.utils import parse_repository_string

def write_file(repository, file_path, filename, content):
    try:
        owner, repo, branch = parse_repository_string(repository)
        clone_dir = f"{settings.GITHUB_CLONE_DIR}/{owner}/{repo}/{branch}"
        fullpath = f"{clone_dir}/{file_path}/{filename}"
        # ensure directory exists
        os.makedirs(os.path.dirname(fullpath), exist_ok=True)
        # write file
        with open(fullpath, 'w') as f:
            f.write(content)
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f'Failed to write file: {str(e)}'}

