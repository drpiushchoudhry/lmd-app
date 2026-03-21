from fastapi import FastAPI, UploadFile, File
import shutil
import os
import cv2

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        os.makedirs("uploads", exist_ok=True)

        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("Saved file:", file_path)

        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            return {"error": "Cannot open video"}

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        cap.release()

        return {
            "status": "success",
            "frames": frame_count
        }

    except Exception as e:
        return {"error": str(e)}