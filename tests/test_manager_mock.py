import pytest
from src.db import DatabaseHandler
from src.manager import HabitManager

@pytest.fixture
def db():
    return DatabaseHandler("data/habits.db")

@pytest.fixture
def mgr(db):
    return HabitManager(db)

def test_mock_habit(mgr, db):
    hid = mgr.create_habit("Mock Habit", "weekly")
    habit = db.find_habit_by_name("Mock Habit")
    assert habit is not None
    assert habit["periodicity"] == "weekly"
    mgr.complete_habit(hid)
    comps = db.fetch_completions()
    assert any(c["habit_id"] == hid for c in comps)
    mgr.delete_habit(hid)

