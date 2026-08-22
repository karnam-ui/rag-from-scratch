import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from retrieval.hybrid_retrieval import HybridRetrieval

retriever = HybridRetrieval()
results = retriever.retrieve("What is the title of the project?", topk=3)
print(results)
