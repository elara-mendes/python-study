# import glob
# import csv
# import shutil
import webbrowser
# myfiles = glob.glob("journal/notes/*.txt")
#
# print(myfiles)
#
# for file in myfiles:
#     with open(file, "r") as text:
#         print(text.read())

# with open("weather.csv", "r") as file:
#     data = list(csv.reader(file))
#
# city = input("Write a city:")
#
# for index, row in enumerate(data):
#     if city in row:
#         print(row[1])
#     # print(index, row)

# print(data)
#
# shutil.make_archive("output", "zip", "journal")

user_search = input("What do you want to search?")

webbrowser.open(f"www.google.com/search?q={user_search}")