import sqlite3
from datetime import datetime
from models.habit import Habit

class DatabaseHandler:
    """
    Handles SQLite operations for habits and completions.
    """

    def __init__(self, db_name="habits.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                periodicity TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                completion_date TEXT NOT NULL,
                FOREIGN KEY (habit_id) REFERENCES habits (id)
            )
        """)
        self.conn.commit()

    def save_habit(self, habit: Habit):
        """Save a new habit to the database."""
        self.cursor.execute("""
            INSERT INTO habits (name, periodicity, created_at)
            VALUES (?, ?, ?)
        """, (habit.name, habit.periodicity, habit.created_at.isoformat()))
        self.conn.commit()

    def load_habits(self):
        """Load all habits from the database."""
        self.cursor.execute("SELECT id, name, periodicity, created_at FROM habits")
        rows = self.cursor.fetchall()
        habits = []
        for row in rows:
            habit = Habit(row[1], row[2])
            habit.created_at = datetime.fromisoformat(row[3])
            habit.id = row[0]  # attach DB id
            habits.append(habit)
        return habits

    def save_completion(self, habit: Habit):
        """Save a completion record for a habit."""
        # Get habit id
        self.cursor.execute("SELECT id FROM habits WHERE name = ?", (habit.name,))
        result = self.cursor.fetchone()
        if result:
            habit_id = result[0]
            self.cursor.execute("""
                INSERT INTO completions (habit_id, completion_date)
                VALUES (?, ?)
            """, (habit_id, datetime.now().isoformat()))
            self.conn.commit()

    def load_completions(self, habit_name: str):
        """Load all completions for a habit."""
        self.cursor.execute("""
            SELECT c.completion_date FROM completions c
            JOIN habits h ON c.habit_id = h.id
            WHERE h.name = ?
        """, (habit_name,))
        rows = self.cursor.fetchall()
        return [datetime.fromisoformat(row[0]) for row in rows]

    def delete_habit(self, habit: Habit):
        """Delete a habit and its completions."""
        self.cursor.execute("DELETE FROM habits WHERE name = ?", (habit.name,))
        self.cursor.execute("""
            DELETE FROM completions WHERE habit_id NOT IN (SELECT id FROM habits)
        """)
        self.conn.commit()
