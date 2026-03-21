def compute_score(metrics):
    score = 100

    # Example logic
    if metrics["motion_score"] > 20:
        score -= 20

    if metrics["frames_sampled"] < 10:
        score -= 10

    return max(score, 0)