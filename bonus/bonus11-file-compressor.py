import PySimpleGUI as psg

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
button1 = psg.FilesBrowse("Choose")

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
button2 = psg.FolderBrowse("Choose")

compress_btn = psg.Button("Compress")

window = psg.Window("File Compressor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [compress_btn]])
window.read()
window.close()