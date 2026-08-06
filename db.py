from pymongo import MongoClient
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    st.error("❌ MongoDB URI not configured. Add MONGO_URI to Streamlit Secrets to enable data persistence.")
    st.stop()

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db = client["hr_copilot"]
    escalation_tickets = db["escalation_tickets"]
    feedback_logs = db["feedback_logs"]
    escalation_tickets.create_index("timestamp")
    feedback_logs.create_index("timestamp")
except Exception as e:
    st.error(f"❌ Failed to connect to MongoDB: {str(e)}")
    st.stop()
