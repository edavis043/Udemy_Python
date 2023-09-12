import modules.todov4func1 as fn
import PySimpleGUI as tk

label = tk.Text("Enter the Todo:")
input_label = tk.InputText(tooltip="Enter the Todo Item.", key="todo")
add_button = tk.Button("Add")
list_box = tk.Listbox(values=fn.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = tk.Button("Edit")

window = tk.Window('ToDo v5.0', layout=[[label], [input_label, add_button], [list_box, edit_button]] )

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case "edit":
            todo_to_edit = values['todos']
            new_todo = values['todo']
            todos = fn.get_todos()
            index = todos.index()
            todos[index] = new_todo
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case tk.WIN_CLOSED:
            break

window.close()
