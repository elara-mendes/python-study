import os

os.makedirs("notes", exist_ok=True)

user_date = input("What's today date?").replace("/", "-")
rate_mood = input("Rate your mood between 1 to 10:")
diary_note = input("Write your thoughts here:")


filepath = f"notes/{user_date}.txt"
if os.path.exists(filepath):
    value = 1
    filepath = f"notes/{user_date}({value})"
    while os.path.exists(filepath):
        value += 1
        filepath = f"notes/{user_date}({value})"

with open(filepath, "w") as file:
    file.writelines(f"Mood: {rate_mood}\nDate: {user_date}\nNote: {diary_note}")

