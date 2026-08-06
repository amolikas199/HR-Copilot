import json
from datetime import datetime

def save_feedback(question, answer, chunks, rating, filename="feedback_log.json"):
    """Save user feedback for analysis."""
    feedback_entry = {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "sources": [{"source": c["source"], "page": c["page"]} for c in chunks],
        "rating": rating,
    }

    try:
        with open(filename, "r") as f:
            feedback = json.load(f)
    except FileNotFoundError:
        feedback = []

    feedback.append(feedback_entry)

    with open(filename, "w") as f:
        json.dump(feedback, f, indent=2)

    return feedback_entry

def get_feedback_stats(filename="feedback_log.json"):
    """Get feedback statistics."""
    try:
        with open(filename, "r") as f:
            feedback = json.load(f)
    except FileNotFoundError:
        return {"total": 0, "helpful": 0, "unhelpful": 0, "ratio": 0}

    total = len(feedback)
    helpful = sum(1 for f in feedback if f["rating"] == "helpful")
    unhelpful = total - helpful

    ratio = (helpful / total * 100) if total > 0 else 0

    return {
        "total": total,
        "helpful": helpful,
        "unhelpful": unhelpful,
        "helpful_ratio": round(ratio, 1)
    }
