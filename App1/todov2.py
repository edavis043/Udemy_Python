todos = []
while True:
    action = input("Type:{add|show|edit|complete|exit}: ")
    action = action.strip()
    match action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'view' | 'display':
            for index, item in enumerate(todos):
                # item = item.title()
                # print(item.capitalize())
                # print(index, '-', item)
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
