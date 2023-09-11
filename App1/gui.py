import modules.todov4func1 as fn
import PySimpleGUI as tk

label = tk.Text("Enter the Todo:")
input_label = tk.InputText(tooltip="Enter the Todo Item.", key="todo")
add_button = tk.Button("Add")

window = tk.Window('ToDo v5.0', layout=[[label], [input_label, add_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
        case tk.WIN_CLOSED:
            break


window.close()
