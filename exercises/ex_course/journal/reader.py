import os

folder = "notes"
files = os.listdir(folder)

for index, file in enumerate(files):
    print(index + 1, "-", file)

user_index = int(input("Write a number:"))
filepath = f"notes/{files[user_index - 1]}"
with open(filepath, "r") as read_mode:
    note = read_mode.read()
    print(note) # I missed the print fn
