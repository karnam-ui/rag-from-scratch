import fitz  # PyMuPDF
import os
class PDFParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        pages = []
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        doc = fitz.open(self.file_path)
        for page in doc:
            indi = {}
            text = page.get_text()
            if not text.strip():  # Check if the page is empty
                text = ""
            
            indi["text"] = text
            indi["page_number"] = page.number + 1
            indi["doc"] = os.path.basename(self.file_path)
            pages.append(indi)
        return pages

    def length(self):
        doc = fitz.open(self.file_path)
        return len(doc)