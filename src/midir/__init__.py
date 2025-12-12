import inspect
import os
import sys
import warnings
from typing import Callable, List


MAX_DEPTH = 50


class FolderNotFoundError(OSError):
    pass


def lsdir(
    path: str,
    return_full_path: bool = True,
    files: bool = True,
    folders: bool = True,
    filter: Callable = None
) -> List[str]:
    real_path = os.path.realpath(path)
    if not os.path.isdir(real_path):
        raise NotADirectoryError(f"'{path}' (searched as '{real_path}')")
    if not (files or folders or filter):
        raise ValueError("Asking for no files or folders, and with no filter?")
    elif (files or folders) and filter:
        warnings.warn(
            "a custom filter was specified but files "
            "and folders parameters are still set to `True`."
        )
    full_paths = [
        os.path.join(real_path if return_full_path else path, object)
        for object in os.listdir(real_path)
    ]
    return sorted([
        full_path for full_path in full_paths
        if (
            (files and os.path.isfile(full_path))
            or (folders and os.path.isdir(full_path))
            or filter is not None and filter(full_path)
        )
    ])


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