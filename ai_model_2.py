from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

def cos_sim(a, b):
    """
    Compute the cosine similarity between two vectors.
    """
    return 1 - cosine(a, b)

# Load the Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Sample sentences for semantic similarity computation
sentences = [
    "The cat sits on the mat",
    "A dog is lying on the rug",
    "The sky is blue",
    "The sun is shining brightly"
]

# Encode the sentences into embeddings
sentence_embeddings = model.encode(sentences)

# Compute pairwise cosine similarity between sentence embeddings
similarities = []
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        similarity = cos_sim(sentence_embeddings[i], sentence_embeddings[j])
        similarities.append((sentences[i], sentences[j], similarity))

# Sort similarities in descending order
similarities.sort(key=lambda x: x[2], reverse=True)

# Print the top N similar sentence pairs
top_n = 5
for i in range(top_n):
    print(f"Similarity between '{similarities[i][0]}' and '{similarities[i][1]}': {similarities[i][2]:.4f}")
