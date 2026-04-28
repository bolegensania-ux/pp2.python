import json

def save_score(name, score, distance):
    try:
        with open("leaderboard.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "name": name,
        "score": int(score),
        "distance": int(distance)
    })

    # keep only top 10
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)