import cv2
import numpy as np

from backend.metrics import compute_metrics
from backend.scoring import compute_score


def process_video(path):
    cap = cv2.VideoCapture(path)

    movements = []
    prev_gray = None

    frame_count = 0
    max_samples = 120   # max number of movement samples (keeps it fast)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # 🔥 Skip frames (process every 5th frame)
        if frame_count % 5 != 0:
            continue

        # 🔥 Resize frame (huge speed boost)
        frame = cv2.resize(frame, (320, 240))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            flow = cv2.calcOpticalFlowFarneback(
                prev_gray,
                gray,
                None,
                0.5,
                3,
                15,
                3,
                5,
                1.2,
                0
            )

            magnitude = np.mean(np.sqrt(flow[..., 0]**2 + flow[..., 1]**2))
            movements.append(magnitude)

        prev_gray = gray

        # 🔥 Stop early to avoid long processing
        if len(movements) >= max_samples:
            break

    cap.release()

    # 🔍 Debug output (check in terminal)
    print(f"Frames sampled: {len(movements)}")

    # Safety fallback
    if len(movements) == 0:
        movements = [0]

    # Compute metrics + score
    metrics = compute_metrics(movements)
    score = compute_score(metrics)

    return {
        "metrics": metrics,
        "score": score
    }