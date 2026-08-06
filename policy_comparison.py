from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from rag import llm

COMPARISON_PROMPT = ChatPromptTemplate.from_template(
    """You are a policy analyst comparing two versions of HR policies.

OLD POLICY:
{old_text}

NEW POLICY:
{new_text}

Analyze the differences and list them as:
- ADDED: <new items or changes>
- REMOVED: <deleted items>
- MODIFIED: <changed items>

Be specific and concise."""
)

def compare_policies(old_file, new_file):
    """Compare two policy PDFs and return differences."""
    try:
        old_loader = PyMuPDFLoader(old_file)
        new_loader = PyMuPDFLoader(new_file)

        old_docs = old_loader.load()
        new_docs = new_loader.load()

        old_text = "\n".join([doc.page_content for doc in old_docs])[:2000]
        new_text = "\n".join([doc.page_content for doc in new_docs])[:2000]

        message = COMPARISON_PROMPT.format(old_text=old_text, new_text=new_text)
        response = llm.invoke(message)

        return response.content
    except Exception as e:
        return f"Error comparing policies: {str(e)}"
