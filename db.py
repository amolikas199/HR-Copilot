from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["hr_copilot"]

escalation_tickets = db["escalation_tickets"]
feedback_logs = db["feedback_logs"]

escalation_tickets.create_index("timestamp")
feedback_logs.create_index("timestamp")
