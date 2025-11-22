import inspect
import os
import sys

def midir(path: str) -> str:
    """
    Returns the directory name of the given path

    Parameters
    ----------
    path: str
        Path to a file or a directory 

    Returns
    -------
    str: Directory name of the given path
    """
    return os.path.dirname(path)

class FolderNotFoundError(OSError):
    """
    Custom exception class to handle the situations when folder is not found
    """
    pass


def get_caller() -> str:
    """
    Returns the filename of the caller

    Returns
    -------
    str: The name of the file that contains the current execution point 
    """
    return inspect.stack()[2].filename

def mipath(path: str = None) -> str:
    """
    Returns the canonical path

    Parameters
    ----------
    path: (str, optional)
        File or directory path. Defaults to None.

    Returns
    -------
    str: Canonical path of the current execution point or given path
    """
    if path is None:
        return os.path.realpath(get_caller())
    else:
        return os.path.realpath(path)

def midir(path: str = None) -> str:
    """
    Returns the directory name from the given path

    Parameters
    ----------
    path: str, optional
        File or directory path. Defaults to None.

    Returns
    -------
    str: Directory name of the current execution point or given path
    """
    if path is None:
        return os.path.dirname(get_caller())
    else:
        return os.path.dirname(path)

def root_levels(levels: int = 1) -> None:
    """
    Adds directories to sys.path
    Starts from the directory of the caller file and move up the directory hierarchy.
    Number of levels to move up is determined by input argument.

    Parameters
    ----------
    levels: int
        Levels to move up the directory hierarchy. Defaults to 1.
    
    Raises
    ------
    TypeError
    ValueError
    """
    folder = midir(get_caller())
    if not isinstance(levels, int):
        raise TypeError(levels)
    elif levels < 0:
        raise ValueError(f'Expects a positive integer: {levels}')
    while levels:
        if folder not in sys.path:
            sys.path.append(folder)
        folder = os.path.dirname(folder)
        levels -= 1

def root_suffix(suffix: str) -> None:
    """
    Adds directories to sys.path
    Starts from the directory of the caller, moves up the directory hierarchy 
    and adds the first folder with the given suffix to sys.path.

    Parameters
    ----------
    suffix: str
        Suffix to match

    Raises
    ------
    TypeError
    ValueError
    FolderNotFoundError: if no folder with the given suffix is found
    """
    if not isinstance(suffix, str):
        raise TypeError(suffix)
    elif not suffix.strip():
        raise ValueError(f'Expects a non-null string: {suffix}')
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