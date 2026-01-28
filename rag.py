import openai
from sentence_transformers import SentenceTransformer
from vector_store import load_vector_store
from config import EMBEDDING_MODEL, OPENAI_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)
index, chunks = load_vector_store()

def answer_question(question, k=5):
    q_emb = model.encode([question])
    _, idx = index.search(q_emb, k)
    context = "\n".join(chunks[i]["text"] for i in idx[0])

    prompt = f"""Answer only from context below.
    If not found, say I don't know.

    Context:
    {context}

    Question: {question}
    """

    res = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return res.choices[0].message.content.strip()