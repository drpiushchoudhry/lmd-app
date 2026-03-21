from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from video_processor import process_video
from scoring import compute_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔥 REAL PROCESSING
        metrics = process_video(file_path)

        # 🔥 SCORING
        score = compute_score(metrics)

        return {
            "status": "success",
            "metrics": metrics,
            "score": score
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}