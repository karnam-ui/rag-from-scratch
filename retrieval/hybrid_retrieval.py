import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from retrieval.dense_retrieval import DenseRetrieval
from retrieval.sparse_retrieval import SparseRetrieval


class HybridRetrieval:
    def __init__(self, file_path="/Users/suhaas/Downloads/Morphex.pdf", chunk_size=100, overlap=20):
        self.sparse_retriever = SparseRetrieval(file_path=file_path, chunk_size=chunk_size, overlap=overlap)
        self.dense_retriever = DenseRetrieval(file_path=file_path, chunk_size=chunk_size, overlap=overlap)

    def retrieve(self, query, topk=10, sparse_topk=10, dense_topk=10):
        sparse_results = self.sparse_retriever.retrieve(query, topk=sparse_topk)
        dense_results = self.dense_retriever.retrieve(query, topk=dense_topk)

        rrf = {}
        for rank, chunk in enumerate(sparse_results, start=1):
            chunk_id = chunk["chunkID"]
            rrf[chunk_id] = {
                "chunkID": chunk_id,
                "text": chunk["text"],
                "doc": chunk["doc"],
                "page_number": chunk["page_number"],
                "score": 1 / (60 + rank),
            }

        for rank, chunk in enumerate(dense_results, start=1):
            chunk_id = chunk["chunkID"]
            if chunk_id in rrf:
                rrf[chunk_id]["score"] += 1 / (60 + rank)
            else:
                rrf[chunk_id] = {
                    "chunkID": chunk_id,
                    "text": chunk["text"],
                    "doc": chunk["doc"],
                    "page_number": chunk["page_number"],
                    "score": 1 / (60 + rank),
                }

        merged_results = []
        for chunk_id, chunk in rrf.items():
            merged_results.append({
                "chunkID": chunk_id,
                "text": chunk["text"],
                "doc": chunk["doc"],
                "page_number": chunk["page_number"],
                "score": float(chunk["score"]),
            })

        sorted_results = sorted(merged_results, key=lambda x: x["score"], reverse=True)[:topk]
        for rank, chunk in enumerate(sorted_results, start=1):
            chunk["rank"] = rank
        return sorted_results

