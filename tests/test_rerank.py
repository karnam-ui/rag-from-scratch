import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from retrieval.rerank import Reranker
from retrieval.hybrid_retrieval import HybridRetrieval

retriever = HybridRetrieval()
retrieved_chunks = retriever.retrieve("What is the title of the project?", topk=5)
reranker = Reranker()
results = reranker.rerank("What is the title of the project?", retrieved_chunks, 3)
print(results)