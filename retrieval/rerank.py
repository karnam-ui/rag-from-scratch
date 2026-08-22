#cross encoder
from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self, model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self, query, chunks,topk):
        cross_encoder_input = [(query, chunk["text"]) for chunk in chunks]

        scores = self.model.predict(cross_encoder_input)

        # Update the results with the new scores
        for i, chunk in enumerate(chunks):
            chunk["CEscore"] = float(scores[i])

        # Sort the results based on the new scores in descending order
        sorted_results = sorted(chunks, key=lambda x: x["CEscore"], reverse=True)

        return sorted_results[:topk]