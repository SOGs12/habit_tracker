from src.analytics import longest_streak_for_habit, longest_streak_all

# Fake habit and completions
habit = {"id": "h1", "name": "Exercise", "periodicity": "daily", "created_at": "2025-12-24T08:00:00"}
completions = [
    {"habit_id": "h1", "completion_date": "2025-12-21T10:00:00"},
    {"habit_id": "h1", "completion_date": "2025-12-22T10:00:00"},
    {"habit_id": "h1", "completion_date": "2025-12-23T10:00:00"},
]

print("Longest streak for Exercise:", longest_streak_for_habit(habit, completions))

habits = [habit]
print("Longest streak overall:", longest_streak_all(habits, completions))

