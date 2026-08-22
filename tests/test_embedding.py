from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

embeddings = model.encode(
    [
        "This is a blue flower from the amazons.",
        "this is a green flower from the amazons.",
        "This is a red apple from the orchard.",
    ]
)

d1 = embeddings[0] @ embeddings[1]
print("Dot product between the first and second embeddings:", d1)
d2 = embeddings[0] @ embeddings[2]
print("Dot product between the first and third embeddings:", d2)
d3 = embeddings[1] @ embeddings[2]
print("Dot product between the second and third embeddings:", d3)