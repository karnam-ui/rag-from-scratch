import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.parser import PDFParser

parser = PDFParser(r"/Users/suhaas/Downloads/Morphex.pdf")
pages = parser.parse()
length = parser.length()
print(pages)
print(length)
