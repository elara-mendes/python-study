import FreeSimpleGUI as sg
import zipfile as zp
import os

text = sg.Text("Which file you want to compress?")
input_label = sg.Input(key="file"), sg.FilesBrowse()
output_label = sg.Input(key="output"), sg.FolderBrowse()
button = sg.Button('Compress')


# Create the window
window = sg.Window('Compressator',
                   layout=[[text], [input_label],
                           [output_label], [button]])

def make_archive(output_path):
    with zp.ZipFile(output_path, "w") as zipf:
        for file in select_file:
            zipf.write(file, os.path.basename(file))

while True:
    events, values = window.read()
    filename = ""
    if events == "Compress":
        filename = sg.popup_get_text("Write the name of the file:")
    output = values["output"]
    file_name = filename + ".zip"
    file_input = values["file"]
    select_file = file_input.split(";")
    output_path = os.path.join(output, file_name)
    make_archive(output_path)
    sg.popup("The file was compressed with success!")

    if events == sg.WIN_CLOSED or events == 'Exit':
        break

window.close()

"""
My teacher is using pathlib
"""
