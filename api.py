
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://jyoti-cloud-mart.puter.site"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

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
