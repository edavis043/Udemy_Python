todos = []
while True:
    action = input("Type:{add|show|edit|complete|exit}: ")
    action = action.strip()

    if 'add' in action or 'new' in action:
        todo = action[4:]
        with open('Files/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')
        with open('Files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in action:
        with open('Files/todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in action:
        number = int(action[5:])
        number = number - 1
        with open('Files/todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter the new item: ")
        todos[number] = new_todo + '\n'
        with open('Files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in action:
        number = int(action[9:])
        with open('Files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_completed = todos[index].strip('\n')
        todos.pop(index)
        with open('Files/todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_completed} marked as completed."

    elif 'exit' in action:
        break

    else:
        print("Invalid Operation!")
print("Saved.")
