from src.db import get_connection

# --- Habit Model Functions ---

def add_habit(name, periodicity, uuid):
    """
    Insert a new habit into the database.
    """
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO habits (name, periodicity, uuid) VALUES (?, ?, ?)",
        (name, periodicity, uuid)
    )
    con.commit()
    con.close()


def get_habits():
    """
    Fetch all habits from the database.
    """
    con = get_connection()
    cur = con.cursor()
    rows = cur.execute(
        "SELECT id, name, periodicity, uuid, created_at FROM habits"
    ).fetchall()
    con.close()
    return rows


def log_habit(habit_id, timestamp):
    """
    Record a completion log for a habit.
    """
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO habit_logs (habit_id, completed_at) VALUES (?, ?)",
        (habit_id, timestamp)
    )
    con.commit()
    con.close()


def delete_habit(habit_id):
    """
    Delete a habit and its logs.
    """
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM habit_logs WHERE habit_id = ?", (habit_id,))
    cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    con.commit()
    con.close()

