from server import mcp
import os
from file_processor.pdf_processor import PDFProcessor
from file_processor.pptx_processor import PPTXProcessor
from file_processor.xlsx_processor import XLSXProcessor


@mcp.resource("greetings://")
def greetings() -> str:
    return "Hello from MCP!"


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
        extension = os.path.splitext(path)[1].lower()
        if extension == ".pdf":
            processor = PDFProcessor()
            result = processor.extract_text_only(path)
            return result["text_content"]
        elif extension == ".pptx":
            processor = PPTXProcessor()
            result = processor.extract_text_only(path)
            return result["text_content"]
        elif extension == ".xlsx":
            processor = XLSXProcessor()
            result = processor.extract_text_only(path)
            return result["text_content"]
        
    except Exception as e:
        return f"Error processing file at {path}: {str(e)}"
