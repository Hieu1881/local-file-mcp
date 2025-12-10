import pypdf
from pypdf import PdfReader
from typing import List, Dict
class PDFProcessor:
    def __init__(self):
        self.max_pages = 3 #Number of max pages to extract

    

    def extract_text_only(self, file_path: str) -> Dict[str, str]:
        reader = PdfReader(file_path)  
        text_content = {}
        for page in min(len(reader.pages), self.max_pages):
            text_content[f"page_{page+1}"] = reader.pages[page].extract_text()
        return {
            "text_content": text_content
        }

    def extract_metadata_only(self, file_path: str) -> Dict[str, Dict[str, str]]:
        reader = PdfReader(file_path)  
        file_metatdata = reader.metadata
        return {
            "metadata": file_metatdata
        }
    def extract_text_and_metadata(self, file_path: str) -> Dict[str, Dict[str, str]]:
        metadata = self.extract_metadata_only(file_path)["metadata"]
        text_content = self.extract_text_only(file_path)["text_content"]
        return {
            "metadata": metadata,
            "text_content": text_content
        }
        