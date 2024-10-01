# # # contents = ['All carrots are to be sliced longitudinally',
# # #             'The carrot is reportedly sliced',
# # #             'The carrot has been transported to the market']
# # #
# # # filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# # #
# # # for content, filename in zip(contents, filenames):
# # #     file = open(f"files/{filename}", 'w')
# # #     file.write(content)
# # date = input("Enter today's date: ")
# # mood = int(input("How do you rate your mood today from 1 to 10? "))
# # thoughts = input("Let your thoughts flow. \n")
# #
# # with open(f"journal/{date}.txt", 'w') as file:
# #     file.write(mood)
# #     file.write(thoughts)
# # check if length is > 8
# # check if there is a digit
# # check if there is an uppercase
# password = input("Enter Password: ")
#
# result = {}
# if len(password) > 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         result["digit"] = True
#     else:
#         result["digit"] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         result["uppercase"] = True
#     else:
#         result["uppercase"] = uppercase
#
# print(result)
# if all(result.values()):
#     print("Strong Password")
# else:
#     print("Weak Password")
#
# def get_average():
#     with open('files/data.txt', 'r') as file:
#         data = file.readlines()
#         values = data[1:]
#         values = [float(i) for i in values]
#         average_local = sum(values)/len(values)
#     return average_local
#
#
# average = get_average()
# print(average)