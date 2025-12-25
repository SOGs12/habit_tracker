import schedule
import time
from models import get_habits

def send_reminder():
    # For simplicity, remind the first user
    user_id = 1
    habits = get_habits(user_id)
    if habits:
        print("\n🔔 Daily Habit Reminder:")
        for habit in habits:
            print(f"- {habit[2]} (Description: {habit[3]})")
    else:
        print("\nNo habits found for reminders.")

# Schedule reminder at 7 AM every day
schedule.every().day.at("07:00").do(send_reminder)

print("✅ Reminder system started...")

while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute
