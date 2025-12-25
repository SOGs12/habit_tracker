from src.db import DatabaseHandler
from src.manager import HabitManager
from src.analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_all,
    longest_streak_for_habit,
)

DB_PATH = "data/habits.db"

def main():
 db = DatabaseHandler(DB_PATH)
 mgr = HabitManager(db)

def menu():
    while True:
        print("\nHabit Tracker - Main Menu")
        print("1) Add a new habit")
        print("2) Complete a habit")
        print("3) View all habits")
        print("4) View analytics")
        print("5) Delete a habit")
        print("0) Exit")

        choice = input("> ").strip().lower()

        if choice in ("0", "exit", "quit", "q"):
            print("👋 Exiting Habit Tracker. Goodbye!")
            break
        elif choice == "1":
            # call create_habit flow
            ...
        elif choice == "2":
            # call complete_habit flow
            ...
        elif choice == "3":
            # call get_habits flow
            ...
        elif choice == "4":
            # call analytics flow
            ...
        elif choice == "5":
            # call delete_habit flow
            ...
        else:
            print("❌ Invalid option, please try again

if __name__ == "__main__":
    main()

