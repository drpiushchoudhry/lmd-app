# Copyright © 2017–2025 Dr. Piush Choudhry / Layveer Medical Division
# All Rights Reserved

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LMD API is LIVE ✅"}

@app.get("/login")
def login():
    return {"status": "secure endpoint placeholder"}