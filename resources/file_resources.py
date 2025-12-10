from server import mcp
import os
from file_processor.pdf_processor import PDFProcessor
from file_processor.pptx_processor import PPTXProcessor
from file_processor.xlsx_processor import XLSXProcessor




@mcp.resource("dir://{path}")
def get_dir_filenames(path: str) -> str:
    """Get a summary of the contents of a directory"""

    try:
        items = os.listdir(path)
        return f"The directory at {path} contains: " + ", ".join(items)
    except FileNotFoundError:
        return f"The directory at {path} does not exist."


@mcp.resource("file://{path}")
def get_file_contents(path: str) -> str:
    try:
        with open(path, "r") as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        return f"The file at {path} does not exist."
