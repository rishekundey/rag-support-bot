import faiss, numpy as np, json
from config import DATA_DIR

def build_vector_store():
    embeddings = np.load(f"{DATA_DIR}/embeddings.npy")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, f"{DATA_DIR}/faiss.index")

def load_vector_store():
    index = faiss.read_index(f"{DATA_DIR}/faiss.index")
    with open(f"{DATA_DIR}/chunks.json") as f:
        chunks = json.load(f)
    return index, chunks