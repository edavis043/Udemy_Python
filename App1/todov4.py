# from todov4func1 import get_todos, write_todos
from modules import todov4func1
import time

time = time.strftime("%b %d, %Y %H:%M")
print("Local Time:", time)

while True:
    action = input("Type:{add|show|edit|complete|exit}: ")
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:]
        todos = todov4func1.get_todos()
        todos.append(todo + '\n')
        todov4func1.write_todos(todos)

    elif action.startswith("show"):
        todos = todov4func1.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            number = number - 1
            todos = todov4func1.get_todos()
            new_todo = input("Enter the new item: ")
            todos[number] = new_todo + '\n'
            todov4func1.write_todos(todos)
        except ValueError:
            print("Invalid Operation!")
            continue

    elif action.startswith("complete"):
        try:
            number = int(action[9:])
            todos = todov4func1.get_todos()
            index = number - 1
            todo_completed = todos[index].strip('\n')
            todos.pop(index)
            todov4func1.write_todos(todos)
            message = f"Todo {todo_completed} marked as completed."
        except IndexError:
            print("No Item Found!")
            continue

    elif action.startswith("exit"):
        break

    else:
        print("Invalid Operation!")
print("Saved.")
