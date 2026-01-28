import json
from config import CHUNK_SIZE, CHUNK_OVERLAP, DATA_DIR

def chunk_text(text):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+CHUNK_SIZE])
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks

def process_text():
    with open(f"{DATA_DIR}/raw_pages.json") as f:
        pages = json.load(f)

    chunks = []
    for page in pages:
        for chunk in chunk_text(page["text"]):
            chunks.append({"text": chunk, "source": page["url"]})

    with open(f"{DATA_DIR}/chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)

if __name__ == "__main__":
    process_text()