import pytest
from src.analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_for_habit,
    longest_streak_all
)

# Sample data in dict format (matches db.fetch_habits / db.fetch_completions)
habits = [
    {"id": "h1", "name": "Drink Water", "periodicity": "daily", "created_at": "2025-12-01"},
    {"id": "h2", "name": "Run", "periodicity": "weekly", "created_at": "2025-12-01"},
]

completions = [
    {"habit_id": "h1", "completion_date": "2025-12-01"},
    {"habit_id": "h1", "completion_date": "2025-12-02"},
    {"habit_id": "h1", "completion_date": "2025-12-03"},
    {"habit_id": "h2", "completion_date": "2025-12-01"},
    {"habit_id": "h2", "completion_date": "2025-12-08"},
]

def test_list_all_habits():
    result = list_all_habits(habits)
    assert result == ["Drink Water", "Run"]

def test_filter_by_periodicity_daily():
    result = filter_by_periodicity(habits, "daily")
    assert len(result) == 1
    assert result[0]["name"] == "Drink Water"

def test_filter_by_periodicity_weekly():
    result = filter_by_periodicity(habits, "weekly")
    assert len(result) == 1
    assert result[0]["name"] == "Run"

def test_longest_streak_for_habit_daily():
    streak = longest_streak_for_habit(habits[0], completions)
    assert streak == 3  # 3 consecutive days

def test_longest_streak_for_habit_weekly():
    streak = longest_streak_for_habit(habits[1], completions)
    assert streak == 2  # 2 consecutive weeks

def test_longest_streak_all():
    hmax, smax = longest_streak_all(habits, completions)
    assert hmax["name"] in ["Drink Water", "Run"]
    assert isinstance(smax, int)
    assert smax >= 2
