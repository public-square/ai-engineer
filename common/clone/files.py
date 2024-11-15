from pathlib import Path
import glob
from django.conf import settings
from common.utils import parse_repository_string

def formatted_files_from_clone(clone, files=False):
    try:
        owner, repo, branch = parse_repository_string(clone)
        clone_dir = Path(f"{settings.GITHUB_CLONE_DIR}/{owner}/{repo}/{branch}")
    except ValueError as e:
        raise Exception(str(e))
    except Exception as e:
        raise Exception(str(e))

    # error if the clone directory does not exist
    if not clone_dir.is_dir():
        raise ValueError(f"Clone directory not found: {clone_dir}")

    # return files
    if not files:
        guardrail = True
        filepaths = clone_dir.rglob('*')
    else:
        guardrail = False
        filepaths=(Path(f"{clone_dir}/{filename}") for filename in files)


    # Store results
    formatted_output = []
    # Walk through directory
    for file_path in filepaths:
        # Skip .git directory
        if ('.git' in str(file_path)):
            continue
        # default to valid if specified, invalid otherwise
        valid_file = not guardrail
        # ignore directories
        if file_path.is_dir():
            valid_file = False
        # accept .md, .py, pyproject.toml, and poetry.lock files
        if (guardrail and (
            file_path.suffix.lower() in settings.VALID_EXTENSIONS or
            file_path.name.lower() in settings.VALID_FILES)):
            valid_file = True
        # check for files with no suffix (potential scripts)
        elif file_path.suffix.lower() == '':
            # Skip if it's a directory
            if not file_path.is_dir():
                try:
                    # Read first line to check for shebang
                    with open(file_path, 'r', encoding='utf-8') as f:
                        first_line = f.readline().strip()
                        if first_line.startswith('#!'):
                            valid_file = True
                except Exception as e:
                    if settings.DEBUG:
                        print(f"Error reading potential script file {file_path}: {str(e)}")

        # exclude files in the ai engineer data directory
        if settings.CLONE_AI_ENGINEER_DIR in str(file_path):
            valid_file = False

        if valid_file:
            try:
                # Read file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Get relative path for cleaner output
                    rel_path = file_path.relative_to(clone_dir)
                    # Format the file information
                    formatted_output.append(f"\nFile: {rel_path}\n")
                    formatted_output.append("```" + (file_path.suffix.lstrip('.')) + "\n")
                    formatted_output.append(content[:3000].strip())
                    formatted_output.append("\n```\n")
            except Exception as e:
                formatted_output.append(f"\nError reading {rel_path}: {str(e)}\n")

    # Join all parts together
    return "".join(formatted_output)

