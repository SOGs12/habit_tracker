from src.models import add_user, get_users, add_habit, get_habits, log_habit, get_logs

def run():
    # Add a user
    add_user("Moses", "moses@example.com")

    # Get users
    users = get_users()
    print("Users:", users)

    # Add a habit for the first user
    user_id = users[0][0]  # first user's ID
    add_habit(user_id, "Morning Run", "Run 5km every morning")

    # Get habits
    habits = get_habits(user_id)
    print("Habits:", habits)

    # Log a habit
    habit_id = habits[0][0]  # first habit's ID
    log_habit(habit_id, "2025-12-21", "Completed")

    # Get logs
    logs = get_logs(habit_id)
    print("Logs:", logs)

if __name__ == "__main__":
    run()
