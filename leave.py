"""
leave.py  —  Module 3 engine: turn a plain-English leave request into JSON.

The new idea here is STRUCTURED OUTPUT: instead of asking the LLM for free
text, we hand it a schema (the LeaveRequest class) and LangChain forces the
model to fill in exactly those fields. So we always get clean, valid data.
"""

from datetime import date
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from rag import llm   # reuse the already-loaded Groq LLM


# --- The schema: the exact shape we want back ---
class LeaveRequest(BaseModel):
    leave_type: str = Field(description="One of: Sick Leave, Casual Leave, Earned Leave, "
                                        "Maternity Leave, Paternity Leave, Unpaid Leave, "
                                        "Bereavement Leave, Work From Home")
    start_date: str = Field(description="Leave start date in YYYY-MM-DD format")
    end_date: str = Field(description="Leave end date in YYYY-MM-DD format")
    reason: str = Field(description="Short reason for the leave, or 'Not specified'")


# with_structured_output() binds the schema to the LLM: every call now returns
# a LeaveRequest object instead of plain text.
extractor = llm.with_structured_output(LeaveRequest)

PROMPT = ChatPromptTemplate.from_template(
    """You extract structured leave-request details from an employee's message.

Today's date is {today}. Use it to resolve relative dates:
- "the 12th to the 16th" means those days in the current month (or the next
  month if they have already passed this month).
- "next Monday", "tomorrow", etc. are relative to today.
Always output dates as YYYY-MM-DD.

Map leave_type to the closest standard category. If the reason implies illness
or medical, use "Sick Leave". If no leave type is clear, use "Casual Leave".
If no reason is given, use "Not specified".

Employee message: {sentence}"""
)


def extract_leave(sentence):
    """Extract the leave request and return it as a plain dict, plus total_days."""
    today = date.today().isoformat()
    message = PROMPT.format(today=today, sentence=sentence)
    result = extractor.invoke(message)     # a LeaveRequest object
    data = result.model_dump()             # convert to a normal dict

    # Compute the number of days in Python (arithmetic is more reliable here
    # than asking the LLM to count).
    try:
        start = date.fromisoformat(data["start_date"])
        end = date.fromisoformat(data["end_date"])
        data["total_days"] = (end - start).days + 1
    except Exception:
        data["total_days"] = None

    return data


# Quick console test:  .venv/Scripts/python.exe leave.py
if __name__ == "__main__":
    print(extract_leave("I need leave from the 12th to the 16th for medical reasons"))
