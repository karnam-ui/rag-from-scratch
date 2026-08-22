import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from ingestion.pipeline import IngestionPipeline


class DenseRetrieval:
    def __init__(self, file_path="/Users/suhaas/Downloads/Morphex.pdf", chunk_size=100, overlap=20, model_name="BAAI/bge-small-en-v1.5"):
        self.pipeline = IngestionPipeline(file_path, chunk_size, overlap)
        self.model = SentenceTransformer(model_name)
        self.chunks = self.pipeline.run()
        assert len(self.chunks) > 0, "No chunks were generated from the PDF file."

    def retrieve(self, query, topk=10):
        texts = [chunk["text"] for chunk in self.chunks]

        embeddings = self.model.encode(texts)
        query_embedding = self.model.encode([query])

        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        scores, indices = index.search(query_embedding, min(topk, len(texts)))

        results = []
        for rank, (score, chunk_index) in enumerate(zip(scores[0], indices[0]), start=1):
            chunk = self.chunks[int(chunk_index)]
            results.append({
                "rank": rank,
                "chunkID": chunk["chunkID"],
                "text": chunk["text"],
                "doc": chunk["doc"],
                "page_number": chunk["page_number"],
                "score": float(score),
            })
        return results


