# waiting_list = ['sen', 'ben', 'john']
# waiting_list.sort(reverse=True)
#
# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)
# member = input('Add a new member: ') + '\n'
# file = open('files/members.txt', 'r')
# members = file.readlines()
# file.close()
#
# members.append(member)
#
# file = open('files/members.txt', 'w')
# file.writelines(members)
# file.close()
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# text = 'Hello'
#
# for filename in zip(filenames):
#     file = open(f"files/{filename}", 'w')
#     file.write(text)
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"files/{filename}", 'r')
    print(file.read())
    file.close()




