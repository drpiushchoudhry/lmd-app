import numpy as np

def normalize(val):
    return float(max(0, min(10, val)))

def compute_metrics(movements):
    if len(movements) == 0:
        movements = [0]

    movements = np.array(movements)

    smoothness = normalize(10 - np.std(movements))
    hesitation = normalize(10 - np.mean(movements < 0.5) * 10)
    flow = normalize(10 - np.var(movements))
    economy = normalize(10 - np.mean(movements))
    technical = normalize(10 - np.max(movements))
    transitions = normalize(10 - np.std(np.diff(movements)))
    consistency = normalize(10 - np.std(movements))
    safety = normalize(10 - np.percentile(movements, 95))
    active_time = normalize(10 - np.mean(movements == 0) * 10)
    integration = normalize(np.mean([smoothness, flow, economy]))

    return {
        "smoothness": smoothness,
        "hesitation": hesitation,
        "flow": flow,
        "economy": economy,
        "technical": technical,
        "transitions": transitions,
        "consistency": consistency,
        "safety": safety,
        "active_time": active_time,
        "integration": integration
    }