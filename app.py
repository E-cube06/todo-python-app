from function import get_todos, write_todos
while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # file = open('todos.txt','r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()sh
        todos = get_todos()

        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()
            print('Here is todos existing', todos)

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            print('Here is how it will be', todos)

            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number - 1]
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('edit'):
        break
    else:
        print("Command is not valid")

