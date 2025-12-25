from src.db import DatabaseHandler

def test_seeded_data():
    db = DatabaseHandler("data/habits.db")
    habits = db.fetch_habits()
    completions = db.fetch_completions()
    # We expect at least 5 habits and many completions
    assert len(habits) >= 5
    assert len(completions) >= 20
    # Check that "Drink water" habit exists
    habit = db.find_habit_by_name("Drink water")
    assert habit is not None
