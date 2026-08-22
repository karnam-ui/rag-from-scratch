from transformers import AutoTokenizer

class TextChunker:
    def __init__(self, chunk_size, overlap):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-small-en-v1.5")

    def chunk(self,text):
        stored_chunks = []
        tokens = self.tokenizer.encode(text, add_special_tokens=False)
        token_count = len(tokens)
        start = 0
        while start<token_count:
            end = min(self.chunk_size+start,token_count)
            chunk_tokens = tokens[start:end]
            chunk_text = self.tokenizer.decode(chunk_tokens)
            stored_chunks.append(chunk_text)
            start += self.chunk_size - self.overlap
        return stored_chunks
