from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import cv2

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "LMD Backend Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        os.makedirs("uploads", exist_ok=True)

        file_path = f"uploads/{file.filename}"

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("Saved file:", file_path)
        print("File exists:", os.path.exists(file_path))
        print("File size:", os.path.getsize(file_path))

        # Try opening video
        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            return {
                "status": "error",
                "message": "OpenCV cannot read this video (codec issue)"
            }

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Read a few frames (to ensure processing works)
        read_frames = 0
        while read_frames < 5:
            ret, frame = cap.read()
            if not ret:
                break
            read_frames += 1

        cap.release()

        return {
            "status": "success",
            "frames": frame_count,
            "fps": fps,
            "sample_frames_read": read_frames
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}