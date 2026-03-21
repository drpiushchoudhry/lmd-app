import cv2

def process_video(path):
    cap = cv2.VideoCapture(path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    motion = 0
    prev = None
    frames_sampled = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev is not None:
            diff = cv2.absdiff(prev, gray)
            motion += diff.mean()

        prev = gray
        frames_sampled += 1

        if frames_sampled > 50:
            break

    cap.release()

    return {
        "frames": frame_count,
        "fps": fps,
        "motion_score": round(motion, 2),
        "frames_sampled": frames_sampled
    }