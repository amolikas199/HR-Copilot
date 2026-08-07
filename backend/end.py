import os

DB_PATH = "../chroma_db"

print("Current working directory:", os.getcwd())
print("Absolute DB path:", os.path.abspath(DB_PATH))
print("Exists:", os.path.exists(DB_PATH))