import sqlite3
from datetime import datetime

sqlite_db_path = "text_chunks.db"

def initialize_database(db_path=sqlite_db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chunks
                      (id INTEGER PRIMARY KEY, text TEXT, timestamp TEXT, title TEXT)''')
    conn.commit()
    conn.close()

def save_chunks_to_sqlite(chunks, db_path=sqlite_db_path, title=""):
    initialize_database(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for chunk in chunks:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO chunks (text, timestamp, title) VALUES (?, ?, ?)", (chunk.page_content, timestamp, title))
    conn.commit()
    conn.close()

def get_documents_by_date(query_date, db_path=sqlite_db_path):
    initialize_database(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT DISTINCT title FROM chunks WHERE DATE(timestamp) = ?"
    cursor.execute(query, (query_date,))
    results = cursor.fetchall()
    conn.close()
    return results

def is_document_uploaded(title, db_path=sqlite_db_path):
    initialize_database(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM chunks WHERE title = ?"
    cursor.execute(query, (title,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0
