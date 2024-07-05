# import glob
#
# myfiles = glob.glob("files/*.txt")
#
# for filepath in myfiles:
#     with open(filepath, "r") as file:
#         print(file.read())
#
# print(myfiles)

# import csv
#
# with open("files/weather.csv", "r") as file:
#     data = list(csv.reader(file))
# print(data)
#
# city = input("Enter a city: ")
# for row in data:
#     if row[0] == city:
#         print(row[1])

# import shutil
#
# shutil.make_archive("output", "zip", "files")

import webbrowser

user_term = input("Enter a search term: ")
webbrowser.open(f"https://google.com/search?q={user_term}")
