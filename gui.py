import modules.functions
import PySimpleGUI as psg

label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo")
input_box2 = psg.InputText(tooltip="Enter todo")
add_btn = psg.Button("Add")

window = psg.Window("To-Do App", layout=[[label], [input_box], [add_btn]])
window.read()
window.close()