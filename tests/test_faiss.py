import numpy as np
import faiss

db = ["The golden retriever chased the red ball across the lawn", "Domestic cats often spend a large portion of the day sleeping in the sun", "Parrots can mimic human speech with remarkable accuracy", "A healthy diet for a puppy includes plenty of protein and fresh water", "Large herds of elephants migrate across the savannah during the dry season", "The local animal shelter rescued ten stray kittens yesterday afternoon", "Aquariums require regular water filtration to keep tropical fish alive", "Training an obedient dog requires patience and consistent positive reinforcement", "Veterinarians recommend annual checkups for aging household pets", "Wild wolves communicate with each other through distant howls."]
query = ["How do I train my new puppy to behave?"]
dimension = 384  # Adjust this based on your embedding dimension

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

db_embeddings = model.encode(db)
query_embedding = model.encode(query)

# Normalize the embeddings
db_embeddings = db_embeddings / np.linalg.norm(db_embeddings, axis=1, keepdims=True)
query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

index = faiss.IndexFlatIP(384)
index.add(db_embeddings)
scores, indices = index.search(query_embedding, 3)

print([scores, indices])