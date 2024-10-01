# # # # def lbs_to_kg(weight):
# # # #     return weight * 0.45
# # # #
# # # #
# # # # def kg_to_lbs(weight):
# # # #     return weight / 0.45
# # # try:
# # #     width = float(input("Enter rectangle width: "))
# # #     length = float(input("Enter rectangle length: "))
# # #     if width == length:
# # #         exit("That looks like a square.")
# # #     area = width * length
# # #     print(area)
# # # except ValueError:
# # #     print("Please enter a number: ")
# # #
# # def calculate_time(h, g=9.80665):
# #     t = (2 * h / g) ** 0.5
# #     return t
# #
# #
# # time = calculate_time(100)
# # print(time)
# from convert14 import convert
# from parsers14 import parse
#
# feet_inches = input("Enter feet and inches: ")
#
# parsed = parse(feet_inches)
#
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide")
import time

date = time.strftime("%b %d, %Y %H:%M:%S")
print(date)
