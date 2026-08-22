import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion.pipeline import IngestionPipeline
from retrieval.sparse_retrieval import SparseRetrieval

retriever = SparseRetrieval()
retriever.retrieve("What is the title of the project?", topk=3)