import sqlite3, os

def init_db():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "habits.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Create tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    periodicity TEXT NOT NULL,
    uuid TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS habit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER NOT NULL,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (habit_id) REFERENCES habits(id)
    )
    """)

    con.commit()
    con.close()

if __name__ == "__main__":
    init_db()
