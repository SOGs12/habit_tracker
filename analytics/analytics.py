def list_all_habits(habits):
    """
    Return all habits.
    Args:
        habits (list): List of Habit objects.
    Returns:
        list: Names of all habits.
    """
    return [habit.name for habit in habits]


def filter_by_periodicity(habits, periodicity):
    """
    Filter habits by periodicity (daily or weekly).
    Args:
        habits (list): List of Habit objects.
        periodicity (str): 'daily' or 'weekly'.
    Returns:
        list: Habits matching the periodicity.
    """
    return [habit.name for habit in habits if habit.periodicity == periodicity]


def longest_streak_all(habits):
    """
    Find the habit with the longest streak overall.
    Args:
        habits (list): List of Habit objects.
    Returns:
        tuple: (habit_name, streak_length)
    """
    if not habits:
        return None, 0

    longest = max(habits, key=lambda h: h.get_streak())
    return longest.name, longest.get_streak()


def longest_streak_for_habit(habit):
    """
    Find the longest streak for a specific habit.
    Args:
        habit (Habit): A Habit object.
    Returns:
        int: Longest streak length.
    """
    return habit.get_streak()
