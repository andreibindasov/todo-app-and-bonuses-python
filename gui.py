import modules.functions as mf
import PySimpleGUI as psg

label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_btn = psg.Button("Add")

window = psg.Window("To-Do App",
                    layout=[[label], [input_box, add_btn]],
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
                mf.update_todos("todos.txt", todos)
        case psg.WINDOW_CLOSED:
            break


window.close()
