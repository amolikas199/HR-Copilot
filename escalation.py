from datetime import datetime
from db import escalation_tickets

ESCALATION_THRESHOLD = 50

def create_ticket(question, confidence, answer):
    """Create an escalation ticket for uncertain queries."""
    ticket = {
        "timestamp": datetime.now(),
        "question": question,
        "confidence": confidence,
        "answer": answer,
        "status": "OPEN",
        "assigned_to": "HR Team"
    }
    return ticket

def save_ticket(ticket):
    """Save escalation ticket to MongoDB."""
    result = escalation_tickets.insert_one(ticket)
    return ticket

def should_escalate(confidence):
    """Check if query should be escalated based on confidence."""
    return confidence < ESCALATION_THRESHOLD

def escalate_query(question, confidence, answer):
    """Escalate a query if confidence is low."""
    if should_escalate(confidence):
        ticket = create_ticket(question, confidence, answer)
        save_ticket(ticket)
        return ticket
    return None

def get_tickets():
    """Get all escalation tickets from MongoDB."""
    return list(escalation_tickets.find().sort("timestamp", -1))
