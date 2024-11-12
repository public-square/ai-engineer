import os
from django.conf import settings
import numpy as np
import array

def list_clones():
    """
    List all local repository clones.

    Returns:
        list: A sorted list of local repository clones in the format owner/repo/branch

    Raises:
        Exception: If there's an error accessing local repository directories
    """
    # Get directories containing local repository clones
    # find /home/grib/ai-engineer-clone/ -maxdepth 4 -name .git
    try:
        findcmd = f"find {settings.GITHUB_CLONE_DIR} -maxdepth 4 -name .git"
        clonedirs = os.popen(findcmd).read().split('\n')
    except Exception as e:
        raise Exception(f"Error accessing local repository directories: {str(e)}")
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

    return list(filter(None, clonedirs))

