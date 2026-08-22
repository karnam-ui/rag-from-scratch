import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.chunker import TextChunker

chunker = TextChunker(chunk_size=200, overlap=40)
chunks = chunker.chunk("This is a sample text that will be chunked into smaller pieces based on the specified chunk size and overlap. The purpose of this test is to ensure that the chunking functionality works as expected and produces the correct number of chunks with the appropriate content.his is a sample text that will be chunked into smaller pieces based on the specified chunk size and overlap. The purpose of this test is to ensure that the chunking functionality works as expected and produces the correct number of chunks with the appropriate content.his is a sample text that will be chunked into smaller pieces based on the specified chunk size and overlap. The purpose of this test is to ensure that the chunking functionality works as expected and produces the correct number of chunks with the appropriate content.his is a sample text that will be chunked into smaller pieces based on the specified chunk size and overlap. The purpose of this test is to ensure that the chunking functionality works as expected and produces the correct number of chunks with the appropriate content.his is a sample text that will be chunked into smaller pieces based on the specified chunk size and overlap. The purpose of this test is to ensure that the chunking functionality works as expected and produces the correct number of chunks with the appropriate content.")
print(chunks)
print(f"Number of chunks: {len(chunks)}")