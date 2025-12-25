import sqlite3, uuid
from datetime import datetime, timedelta

DB_PATH = "data/habits.db"

def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

def insert_habit(cur, name, periodicity, created_at):
    hid = str(uuid.uuid4())
    cur.execute(
        "INSERT INTO habits (id, name, periodicity, created_at) VALUES (?,?,?,?)",
        (hid, name, periodicity, created_at),
    )
    return hid

def insert_completion(cur, hid, dt):
    cur.execute(
        "INSERT INTO completions (habit_id, completion_date) VALUES (?,?)",
        (hid, iso(dt)),
    )

def main():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    # Clear existing data safely
    cur.execute("DELETE FROM completions;")
    cur.execute("DELETE FROM habits;")

    base = datetime(2025, 11, 3, 8, 0, 0)  # Monday start

    # Habits
    h1 = insert_habit(cur, "Drink water", "daily", iso(base))
    h2 = insert_habit(cur, "Exercise", "daily", iso(base))
    h3 = insert_habit(cur, "Call parents", "weekly", iso(base))
    h4 = insert_habit(cur, "Clean room", "weekly", iso(base))
    h5 = insert_habit(cur, "Review goals", "weekly", iso(base))

    # Daily: Drink water (28 days straight)
    for i in range(28):
        insert_completion(cur, h1, base + timedelta(days=i, hours=7))

    # Daily: Exercise (gap after week 1)
    for i in range(7):
        insert_completion(cur, h2, base + timedelta(days=i, hours=18))
    for i in range(9, 28):   # <-- fixed indentation here
        insert_completion(cur, h2, base + timedelta(days=i, hours=18))

    # Weekly: Call parents (4 consecutive weeks)
    for w in range(4):
        insert_completion(cur, h3, base + timedelta(days=w*7, hours=19))

    # Weekly: Clean room (miss week 2)
    insert_completion(cur, h4, base + timedelta(days=0, hours=12))
    insert_completion(cur, h4, base + timedelta(days=14, hours=12))
    insert_completion(cur, h4, base + timedelta(days=21, hours=12))

    # Weekly: Review goals (multiple completions per week)
    for w in range(4):
        monday = base + timedelta(days=w*7)
        insert_completion(cur, h5, monday + timedelta(hours=9))
        insert_completion(cur, h5, monday + timedelta(days=2, hours=9))

    con.commit()
    con.close()
    print("Seeded 5 habits with 4 weeks of data.")

if __name__ == "__main__":
    main()

