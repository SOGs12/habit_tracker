import sqlite3
from typing import List, Dict, Optional
import os

class DatabaseHandler:
    def __init__(self, path: str = "data/habits.db"):
        self.path = path

    def _conn(self):
        con = sqlite3.connect(self.path)
        con.execute("PRAGMA foreign_keys = ON")
        return con

    def insert_habit(self, hid: str, name: str, periodicity: str, created_at: str) -> None:
        con = self._conn()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO habits (id, name, periodicity, created_at) VALUES (?,?,?,?)",
            (hid, name, periodicity, created_at),
        )
        con.commit()
        con.close()

    def insert_completion(self, hid: str, ts: str) -> None:
        con = self._conn()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO completions (habit_id, completion_date) VALUES (?,?)",
            (hid, ts),
        )
        con.commit()
        con.close()

    def fetch_habits(self) -> List[Dict]:
        con = self._conn()
        cur = con.cursor()
        cur.execute("SELECT id, name, periodicity, created_at FROM habits")
        rows = cur.fetchall()
        con.close()
        return [
            {"id": r[0], "name": r[1], "periodicity": r[2], "created_at": r[3]}
            for r in rows
        ]

    def fetch_completions(self) -> List[Dict]:
        con = self._conn()
        cur = con.cursor()
        cur.execute("SELECT habit_id, completion_date FROM completions")
        rows = cur.fetchall()
        con.close()
        return [
            {"habit_id": r[0], "completion_date": r[1]}
            for r in rows
        ]

    def delete_habit(self, hid: str) -> bool:
        con = self._conn()
        cur = con.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (hid,))
        changed = cur.rowcount > 0
        con.commit()
        con.close()
        return changed

    def find_habit_by_name(self, name: str) -> Optional[Dict]:
        con = self._conn()
        cur = con.cursor()
        row = cur.execute(
            "SELECT id, name, periodicity, created_at FROM habits WHERE name = ? LIMIT 1",
            (name,),
        ).fetchone()
        con.close()
        if not row:
            return None
        return {"id": row[0], "name": row[1], "periodicity": row[2], "created_at": row[3]}


def init_db():
    """Initialize the database schema (habits + completions tables)."""
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    db_path = os.path.join(data_dir, "habits.db")

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        periodicity TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS completions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id TEXT NOT NULL,
        completion_date TEXT NOT NULL,
        FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
    )
    """)

    con.commit()
    con.close()
    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()

