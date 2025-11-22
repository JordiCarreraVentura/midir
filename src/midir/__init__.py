import inspect
import os
import sys


"""
def midir(path: str) -> str:
    return os.path.dirname(path)
"""

class FolderNotFoundError(OSError):
    pass


def get_caller() -> str:
    return inspect.stack()[2].filename

def mipath(path: str = None) -> str:
    if path is None:
        return os.path.realpath(get_caller())
    else:
        return os.path.realpath(path)

def midir(path: str = None) -> str:
    if path is None:
        return os.path.dirname(get_caller())
    else:
        return os.path.dirname(path)

def root_levels(levels=1) -> None:
    folder = midir(get_caller())
    while levels:
        if folder not in sys.path:
            sys.path.append(folder)
        folder = os.path.dirname(folder)
        levels -= 1

def root_suffix(suffix: str) -> None:
    folder = midir(get_caller())
    while True:
        if (
            os.path.basename(folder).endswith(suffix)
            and folder not in sys.path
        ):
            sys.path.append(folder)
            return
        folder = os.path.dirname(folder)
        if folder == '/':
            raise FolderNotFoundError(suffix)

