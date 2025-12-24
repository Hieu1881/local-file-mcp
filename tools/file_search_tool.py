from server import mcp
import os

@mcp.tool()
def file_search_by_name(directory: str, filename: str) -> str:
    """Search for a file by name in a given directory and its subdirectories.

    Args:
        directory (str): The directory to search in.
        filename (str): The name of the file to search for.

    Returns:
        str: The full path of the found file or a message indicating it was not found.
    """
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return f"File '{filename}' not found in directory '{directory}'."
