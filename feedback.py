from datetime import datetime
from db import feedback_logs

def save_feedback(question, answer, chunks, rating):
    """Save user feedback to MongoDB."""
    feedback_entry = {
        "timestamp": datetime.now(),
        "question": question,
        "answer": answer,
        "sources": [{"source": c["source"], "page": c["page"]} for c in chunks],
        "rating": rating,
    }
    feedback_logs.insert_one(feedback_entry)
    return feedback_entry

def get_feedback_stats():
    """Get feedback statistics from MongoDB."""
    feedback_list = list(feedback_logs.find())

    if not feedback_list:
        return {"total": 0, "helpful": 0, "unhelpful": 0, "helpful_ratio": 0}

    total = len(feedback_list)
    helpful = sum(1 for f in feedback_list if f.get("rating") == "helpful")
    unhelpful = total - helpful
    ratio = (helpful / total * 100) if total > 0 else 0

    return {
        "total": total,
        "helpful": helpful,
        "unhelpful": unhelpful,
        "helpful_ratio": round(ratio, 1)
    }

def get_feedback_entries():
    """Get all feedback entries from MongoDB."""
    return list(feedback_logs.find().sort("timestamp", -1))
