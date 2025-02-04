import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple1")
clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo item", key="todo")
add_button = sg.Button(image_size=(40, 25), image_source="add.png", key="Add", tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button(key="Edit", image_size=(40, 25), image_source='edit.png', tooltip="Edit Todo")
complete_button = sg.Button(key="Complete", image_size=(40, 25), image_source='complete.png', tooltip="Complete Todo")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=200)
    if event in (None, 'exit', sg.WIN_CLOSED):
        break
    if values is not None:
        window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
        match event:
            case "Add":
                todos = functions.get_todos()
                if values['todo'].strip() == "":
                    sg.popup("Please type a todo before clicking Add.", font=("Helvetica", 10))
                    window['todo'].update(value='')
                else:
                    new_todo = values['todo'] + "\n"
                    todos.append(new_todo)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
            case "Edit":
                try:
                    todo_to_edit = values['todos'][0]
                    new_todo = values['todo'] + "\n"
                    todos = functions.get_todos()
                    todo_index = todos.index(todo_to_edit)
                    todos[todo_index] = new_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                except IndexError:
                    sg.Popup("Please select an item first", font=("Helvetica", 12))
            case "Complete":
                try:
                    todo_to_complete = values["todos"][0]
                    todos = functions.get_todos()
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.Popup("Please select an item first", font=("Helvetica", 12))
            case 'todos':
                window['todo'].update(value=values['todos'][0])
            case "Exit":
                break
            case sg.WIN_CLOSED:
                break

window.close()
