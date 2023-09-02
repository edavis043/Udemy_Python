def get_todos():
    with open('../Files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg):
    with open('../Files/todos.txt', 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Items List:")
    print(get_todos())
