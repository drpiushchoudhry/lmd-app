from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LMD backend is LIVE 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}