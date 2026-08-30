from pydoc import doc

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

    def extract_tables(self):
        doc = fitz.open(self.file_path)

        for page in doc:
            tables = page.find_tables()

            print(f"Page {page.number + 1}: {len(tables.tables)} tables")

            for table in tables.tables:
                print(table.extract())
                
    def inspect_words(self, page_number=1):
        doc = fitz.open(self.file_path)
        page = doc[page_number - 1]

        words = page.get_text("words")

        for word in words:
            print(word)