from datetime import datetime, timezone
import uuid
from .db import DatabaseHandler

class HabitManager:
    def __init__(self, db: DatabaseHandler):
        self.db = db

    def create_habit(self, name: str, periodicity: str):
        """Create a new habit with a unique ID and save it to the database."""
        if not name.strip():
            raise ValueError("Habit name cannot be empty.")
        if periodicity not in ("daily", "weekly"):
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")
        hid = str(uuid.uuid4())
        created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        self.db.insert_habit(hid, name.strip(), periodicity, created_at)
        return hid

    def delete_habit(self, hid: str) -> bool:
        """Delete a habit by its ID."""
        return self.db.delete_habit(hid)

    def complete_habit(self, hid: str):
        """Mark a habit as completed at the current time."""
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        self.db.insert_completion(hid, ts)
        return ts


