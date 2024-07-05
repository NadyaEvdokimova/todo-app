# password = input("Enter new password: ")
# result = {}
# if len(password) >= 8:
#     result["Length"] = True
# else:
#     result["Length"] = False
#
# digit = False
# for char in password:
#     if char.isdigit():
#         digit = True
#
# result["Digit"] = digit
#
# upper = False
# for char in password:
#     if char.isupper():
#         upper = True
# result["Uppercase"] = upper
#
# if all(result.values()):
#     print("Strong password")
# else:
#     print("Weak password")
#
# print(result)
from parsers import parse, convert

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[-3:])

# try:
#     width = float(input("Enter rectangle width: "))
#     length = float(input("Enter rectangle length: "))
#     if width == length:
#         exit("That looks like a square.")
#     area = width * length
# except ValueError:
#     print("Please enter a number.")

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     percentage = value/total_value * 100
#     print(f"That is {percentage}")
# except ValueError:
#     print("You need to enter a number. Run the program again.")
# except ZeroDivisionError:
#     print("Your total value cannot be zero.")

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# try:
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f"{name} is not in the list.")

# def get_average():
#     with open("files/data.txt", "r") as file:
#         data = file.readlines()
#     values = data[1:]
#     values = [float(item) for item in values]
#     average_local = sum(values) / len(values)
#     return average_local
#
#
# average = get_average()
# print(average)

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_grade = max(grades)
#     min_grade = min(grades)
#     return f"Max: {max_grade}, Min: {min_grade}"
#
#
# answer = get_max()
# print(answer)

# contents = ["first item", "second item", "third item"]
# filenames = ["first.txt", "second.txt", "third"]
#
# for content, filename in zip(contents, filenames):
#     with open(filename, "w") as file:
#         file.write(content)

# feel_inches = input("Enter feet and inches: ")
#
# parsed = parse(feel_inches)
# result = convert(parsed["feet"], parsed["inches"])
# print(f"{parsed["feet"]} feet and {parsed["inches"]} is equal to {result} meters")
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")

# def get_nr_times(text):
#     text_list = text.split(",")
#     text_len = len(text_list)
#     return text_len
#
# print(get_nr_times("Hghs, ghgsd, hgdsh"))


