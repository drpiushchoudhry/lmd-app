from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LMD backend is LIVE 🚀"}

@app.get("/test")
def test():
    return {"status": "ok"}

handler = Mangum(app)