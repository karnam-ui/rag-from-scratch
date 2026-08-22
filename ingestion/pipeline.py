import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.parser import PDFParser
from ingestion.chunker import TextChunker

class IngestionPipeline:
    def __init__(self, file_path, chunk_size, overlap):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.parser = PDFParser(file_path)
        self.chunker = TextChunker(chunk_size, overlap)

    def run(self):
        pages = self.parser.parse()
        all_chunks = []
        chunkID = 1
        for page in pages:
            text = page["text"]
            chunks = self.chunker.chunk(text)
            for chunk in chunks:
                indi = {}
                indi["text"] = chunk
                indi["chunkID"] = chunkID
                chunkID += 1
                indi["page_number"] = page["page_number"]
                indi["doc"] = page["doc"]
                all_chunks.append(indi)
        return all_chunks
