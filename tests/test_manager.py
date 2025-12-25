import pytest
from src.db import DatabaseHandler
from src.manager import HabitManager

@pytest.fixture
def db():
    return DatabaseHandler("data/habits.db")

@pytest.fixture
def mgr(db):
    return HabitManager(db)

def test_create_and_delete_habit(mgr, db):
    hid = mgr.create_habit("Test Habit", "daily")
    habit = db.find_habit_by_name("Test Habit")
    assert habit is not None
    assert habit["id"] == hid
    assert mgr.delete_habit(hid) is True

def test_complete_habit(mgr, db):
    hid = mgr.create_habit("Temp Habit", "daily")
    ts = mgr.complete_habit(hid)
    completions = db.fetch_completions()
    assert any(c["habit_id"] == hid for c in completions)
    mgr.delete_habit(hid)

