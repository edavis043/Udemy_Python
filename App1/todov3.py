todos = []
while True:
    action = input("Type:{add|show|edit|complete|exit}: ")
    action = action.strip()
    match action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('Files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'view' | 'display':
            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # new_todos = []
            # for item in new_todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item) OR
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                # item = item.title()
                # print(item.capitalize())
                # print(index, '-', item)
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        #   print("hello", index, item) #shows the last value in loop
        case 'edit':
            number = int(input("Enter the Todo number: "))
            number = number - 1
            new_todo = input("Enter the new item: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter the completed todo: "))
            todos.pop(number - 1)
        case 'exit':
            break
        # case invalid:
        #     print("Invalid Operation!")
print("Saved.")
