import modules.functions as mf
import PySimpleGUI as psg

label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_btn = psg.Button("Add")

list_box = psg.Listbox(values=mf.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 12])
edit_btn = psg.Button("Edit")

# btn_labels = ["Close", "Submit"]
# layout = []
# for bl in btn_labels:
#     layout.append(psg.Button(bl))

layout = [[label], [input_box, add_btn], [list_box, edit_btn]]

window = psg.Window("To-Do App",
                    layout=layout,
                    font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
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
            if len(values['todos']) > 0:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = mf.get_todos()
                idx = todos.index(todo_to_edit)
                todos[idx] = new_todo + '\n'
                mf.update_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
        case "todos":
            if len(values['todos']) > 0:
                window['todo'].update(value=values['todos'][0].strip("\n"))
        case psg.WINDOW_CLOSED:
            break
            # exit() - stop the program completely

window.close()
