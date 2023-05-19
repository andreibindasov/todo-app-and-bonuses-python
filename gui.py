import modules.functions as mf
import PySimpleGUI as psg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as f:
        pass

psg.theme("Black")

label_clock = psg.Text('', key='clock')
label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_btn = psg.Button("Add", button_color=("white", "grey"), size=12)
# add_btn = psg.Button(size=6, image_source="add.png",
#                      mouseover_colors="LightBlue2",
#                      tooltip="Add a new todo", key="Add")

list_box = psg.Listbox(values=mf.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 12])
edit_btn = psg.Button("Edit", button_color=("white", "grey"), size=12)

complete_btn = psg.Button("Complete", button_color=("white", "green"), size=12)

exit_btn = psg.Button("Exit", button_color=("white", "purple"), size=75)
# btn_labels = ["Close", "Submit"]
# layout = []
# for bl in btn_labels:
#     layout.append(psg.Button(bl))

layout = [[label_clock],
          [label],
          [input_box, add_btn],
          [list_box, edit_btn, complete_btn],
          [exit_btn]]

window = psg.Window("To-Do App",
                    layout=layout,
                    font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = mf.get_todos()
            new_todo = values['todo'].strip() + "\n"
            if new_todo != "":
                todos.append(new_todo)
                mf.update_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = mf.get_todos()
                idx = todos.index(todo_to_edit)
                todos[idx] = new_todo + '\n'
                mf.update_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                psg.popup("Please, select a todo", font=('Helvetica', 18))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = mf.get_todos()
                todos.remove(todo_to_complete)
                mf.update_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup("Please, select a todo to complete!", font=('Helvetica', 18))
        case "Exit":
            break
        case "todos":
            if len(values['todos']) > 0:
                window['todo'].update(value=values['todos'][0].strip("\n"))
        case psg.WINDOW_CLOSED:
            break
            # exit() - stop the program completely

window.close()
