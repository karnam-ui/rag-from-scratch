import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from retrieval.context_builder import ContextBuilder

context_builder = ContextBuilder()
context, reranked_results = context_builder.build_context("What is the title of the project?", topk=5, rerank_topk=2)
print("Context:\n", context)
print("Reranked Results:\n", reranked_results)