from datetime import datetime
import json

ESCALATION_THRESHOLD = 50

def create_ticket(question, confidence, answer):
    """Create an escalation ticket for uncertain queries."""
    ticket = {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "confidence": confidence,
        "answer": answer,
        "status": "OPEN",
        "assigned_to": "HR Team"
    }
    return ticket

def save_ticket(ticket, filename="escalation_tickets.json"):
    """Save escalation ticket to file."""
    try:
        with open(filename, "r") as f:
            tickets = json.load(f)
    except FileNotFoundError:
        tickets = []

    tickets.append(ticket)

    with open(filename, "w") as f:
        json.dump(tickets, f, indent=2)

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
