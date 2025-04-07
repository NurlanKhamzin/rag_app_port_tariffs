
import faiss
import numpy as np

def create_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def query_faiss_index(query_embedding, index, texts, top_k=3):
    _, results = index.search(np.array([query_embedding]), k=top_k)
    return [texts[i] for i in results[0]]