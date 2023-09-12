import modules.todov4func1 as fn
import PySimpleGUI as tk
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

tk.theme("DarkTeal12")
clock = tk.Text('', key='clock')
label = tk.Text("Enter the Todo:")
input_label = tk.InputText(key="todo")
add_button = tk.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Item", key="Add")   # add_button = tk.Button("Add")
list_box = tk.Listbox(values=fn.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = tk.Button("Edit")
complete_button = tk.Button("Complete")
exit_button = tk.Button("Exit")
window = tk.Window('ToDo v5.0',
                   layout=[[clock],
                           [label],
                           [input_label, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 14))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M"))
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                tk.popup("Please select an Item!", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_remove = values['todos'][0]
                todos = fn.get_todos()
                todos.remove(todo_to_remove)
                fn.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(values='')
            except IndexError:
                tk.popup("Please select an Item!", font=("Helvetica", 14))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case tk.WIN_CLOSED:
            break

window.close()
