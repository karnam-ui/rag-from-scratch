import re

import numpy as np

from ingestion.pipeline import IngestionPipeline


class SparseRetrieval:
    def __init__(self, file_path="/Users/suhaas/Downloads/Morphex.pdf", chunk_size=100, overlap=20):
        self.pipeline = IngestionPipeline(file_path, chunk_size, overlap)
        self.chunks = self.pipeline.run()
        assert len(self.chunks) > 0, "No chunks were generated from the PDF file."

    @staticmethod
    def tokenizer(text):
        return re.findall(r"\b\w+\b", text.lower())

    def retrieve(self, query, topk=10):
        corpus = [chunk["text"] for chunk in self.chunks]
        chunkslen = len(self.chunks)
        if chunkslen == 0:
            return []

        doc_freq = {}
        tokenized_corpus = []
        for text in corpus:
            tokens = self.tokenizer(text)
            tokenized_corpus.append(tokens)
            for word in set(tokens):
                doc_freq[word] = doc_freq.get(word, 0) + 1

        avgdl = sum(len(tokens) for tokens in tokenized_corpus) / chunkslen
        query_words = self.tokenizer(query)

        scored_chunks = []
        for i, chunk in enumerate(self.chunks):
            chunk_score = 0.0
            for word in query_words:
                if word in tokenized_corpus[i]:
                    tf = tokenized_corpus[i].count(word)
                    idf = np.log((chunkslen - doc_freq.get(word, 0) + 0.5) / (doc_freq.get(word, 0) + 0.5) + 1)
                    score = (tf * (1.5 + 1)) / (tf + 1.5 * (1 - 0.75 + 0.75 * len(tokenized_corpus[i]) / avgdl)) * idf
                    chunk_score += score

            scored_chunks.append({
                **chunk,
                "score": float(chunk_score),
            })

        sorted_chunks = sorted(scored_chunks, key=lambda x: x["score"], reverse=True)
        results = []
        for rank, chunk in enumerate(sorted_chunks[:topk], start=1):
            results.append({
                "rank": rank,
                "chunkID": chunk["chunkID"],
                "text": chunk["text"],
                "doc": chunk["doc"],
                "page_number": chunk["page_number"],
                "score": chunk["score"],
            })
        return results
