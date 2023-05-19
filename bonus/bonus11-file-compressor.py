import PySimpleGUI as psg
from zip_creator import make_archive

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
button1 = psg.FilesBrowse("Choose", key="files")

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
button2 = psg.FolderBrowse("Choose", key="folder")

compress_btn = psg.Button("Compress")
output_label = psg.Text(key="output", text_color="yellow")

window = psg.Window("File Compressor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [compress_btn, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")
    # if not psg.WINDOW_CLOSED:
    #     continue
    # break

window.close()
