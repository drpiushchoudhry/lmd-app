from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LMD backend is LIVE 🚀"}

handler = Mangum(app)