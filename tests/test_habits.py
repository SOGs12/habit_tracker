import pytest
from src.db import DatabaseHandler
from src.manager import HabitManager
from src.analytics import longest_streak_for_habit, longest_streak_all

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
    deleted = mgr.delete_habit(hid)
    assert deleted is True

def test_complete_habit(mgr, db):
    hid = mgr.create_habit("Temp Habit", "daily")
    ts = mgr.complete_habit(hid)
    completions = db.fetch_completions()
    assert any(c["habit_id"] == hid for c in completions)
    mgr.delete_habit(hid)

def test_longest_streak(db):
    habits = db.fetch_habits()
    completions = db.fetch_completions()
    hmax, smax = longest_streak_all(habits, completions)
    assert hmax is not None
    assert isinstance(smax, int)
    # Check streak for Drink water
    habit = db.find_habit_by_name("Drink water")
    streak = longest_streak_for_habit(habit, completions)
    assert streak >= 28

