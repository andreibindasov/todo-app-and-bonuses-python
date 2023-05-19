import PySimpleGUI as psg
from zip_extractor import extract_archive

psg.theme("Black")

label1 = psg.Text("Select archive:", size=21)
input1 = psg.Input(size=45)
choose1 = psg.FileBrowse("Choose", key="archive")

label2 = psg.Text("Select destination: ", size=21)
input2 = psg.Input(size=45)
choose2 = psg.FolderBrowse("Choose", key="folder")

extract_btn = psg.Button("Extract", key="extract")
label_output = psg.Text(key="output", text_color="green")

window = psg.Window("Archive Extractor",
                    layout=[[label1, input1, choose1],
                            [label2, input2, choose2],
                            [extract_btn, label_output]])

while True:
    try:
        event, values = window.read()
        extract_archive(values['archive'], values['folder'])
        window['output'].update(value='Extraction completed!')
    except:
        break

window.close()
