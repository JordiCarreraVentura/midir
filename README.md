# midir

A library for resolving relative module dependencies.

# Description

`midir` is a Python library designed to handle relative module dependencies by resolving directory paths in an intelligent and system-agnostic way. This library can be used to introspect the file structure of your project and manipulate Python's `sys.path`, allowing for dynamic module imports based on directory hierarchy. It is especially helpful for larger projects where file structure can become complex and static imports cumbersome to manage. 

## Features

1. `midir(path: str) -> str:` Returns the directory name of the given file or directory path.

2. `get_caller() -> str:` Returns the name of the file or the location (directory) where the current execution point is present.

3. `mipath(path: str = None) -> str:` Returns the canonical (absolute) path of the current execution point or a provided path.

4. `midir(path: str = None) -> str:` Returns the directory name where the current execution point is or from a provided path.

5. `root_levels(levels: int = 1) -> None:` Makes directories available for import by adding them to sys.path. It starts from directory of the caller file and move up the directory hierarchy. The number of levels up to move is determined by input argument.

6. `root_suffix(suffix: str) -> None:` Similar to `root_levels`, but instead of moving up a certain number of directories, it continues to move up until it finds a directory whose name ends with the provided suffix and adds that directory to sys.path.

## Exceptions

1. `FolderNotFoundError:` Custom exception raised when no folder matching the required conditions (in `root_suffix`) is found in the directory hierarchy.

## Build instructions

1. Building the package before uploading: 'python -m build' (from "midir").
2. Upload the package to pypi: 'python -m twine upload --repository pypi dist/*'
3. Install the package from pypi: 'python -m pip install midir'
4. If any dependencies are required, edit the `pyproject.toml` file, "\[project\]" field, and add a `dependencies` key with a `List\[str\]` value, where each string is a `pip`-readable dependency.
