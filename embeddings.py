from sentence_transformers import SentenceTransformer
import json, numpy as np
from config import EMBEDDING_MODEL, DATA_DIR

model = SentenceTransformer(EMBEDDING_MODEL)

with open(f"{DATA_DIR}/chunks.json") as f:
    chunks = json.load(f)

texts = [c["text"] for c in chunks]
embeddings = model.encode(texts, show_progress_bar=True)

np.save(f"{DATA_DIR}/embeddings.npy", embeddings)