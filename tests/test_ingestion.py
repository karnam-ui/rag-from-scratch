import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline(r"/Users/suhaas/Downloads/Morphex.pdf", 100, 20)
chunks = pipeline.run()
for chunk in chunks:
    print(chunk)
    print("---------------------------------")

