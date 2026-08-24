import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from retrieval.rerank import Reranker
from retrieval.hybrid_retrieval import HybridRetrieval

class ContextBuilder:
    def __init__(self):
        self.retriever = HybridRetrieval()
        self.reranker = Reranker()

    def build_context(self, query, topk=5, rerank_topk=3):
        retrieved_chunks = self.retriever.retrieve(query, topk=topk)
        reranked_results = self.reranker.rerank(query, retrieved_chunks, rerank_topk)
        context = []
        for i, result in enumerate(reranked_results):
            individual_results = ""
            individual_results += "--------------------------------\n"
            individual_results += f"Source: {i + 1}\n"
            individual_results += f"Chunk: {result['chunkID']}\n"
            individual_results += f"Page: {result['page_number']}\n"
            individual_results += f"Doc: {result['doc']}\n"
            individual_results += f"Text: {result['text']}\n"
    
            context.append(individual_results)

        return "\n\n".join(context),reranked_results







