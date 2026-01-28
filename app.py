from fastapi import FastAPI
from rag import answer_question

app = FastAPI()

@app.post("/ask")
def ask(question: str):
    return {"answer": answer_question(question)}