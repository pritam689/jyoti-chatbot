
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Jyoti Cloud Mart API! 🌸"}

@app.get("/chat")
def chat(question: str):
    question = question.lower()

    if "saree" in question:
        answer = "Welcome to our beautiful saree collection! 🌸"
    else:
        answer = "Hello! Welcome to Jyoti Cloud Mart!"

    return {"answer": answer}
