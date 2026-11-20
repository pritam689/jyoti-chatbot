@app.get("/chat")
def chat(question: str):
    question = question.lower()

    if "saree" in question:
        answer = "Welcome to our beautiful saree collection! 🌸"
    else:
        answer = "Hello! Welcome to Jyoti Cloud Mart!"

    return {"answer": answer}