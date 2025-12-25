import click
from managers.habit_manager import HabitManager
from analytics.analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_all,
    longest_streak_for_habit
)

manager = HabitManager()

@click.group()
def cli():
    """Habit Tracker CLI"""
    pass

@cli.command()
@click.argument("name")
@click.argument("periodicity")
def add(name, periodicity):
    """Add a new habit"""
    manager.create_habit(name, periodicity)

@cli.command()
def list():
    """List all habits"""
    manager.list_habits()

@cli.command()
@click.argument("name")
def complete(name):
    """Complete a habit"""
    manager.complete_habit(name)

@cli.command()
@click.argument("name")
def delete(name):
    """Delete a habit"""
    manager.delete_habit(name)

@cli.command()
def analytics():
    """View analytics"""
    habits = manager.habits
    print("All habits:", list_all_habits(habits))
    print("Daily habits:", filter_by_periodicity(habits, "daily"))
    print("Weekly habits:", filter_by_periodicity(habits, "weekly"))
    print("Longest streak overall:", longest_streak_all(habits))
    if habits:
        print("Longest streak for first habit:", longest_streak_for_habit(habits[0]))

if __name__ == "__main__":
    cli()