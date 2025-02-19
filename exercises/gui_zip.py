import FreeSimpleGUI as sg
import zipfile as zp
import os

text = sg.Text("Which file you want to compress?")
input_label = sg.Input(key="file"), sg.FilesBrowse()
output_label = sg.Input(key="output"), sg.FolderBrowse()
button = sg.Button('Compress')

# Create the window
window = sg.Window('Compressator', layout=[[text], [input_label], [output_label], [button]])

events, values = window.read()

output = values["output"]
file_name = "my_file.zip"
file_input = values["file"]
select_file = file_input.split(";")
output_path = os.path.join(output, file_name)
with zp.ZipFile(output_path, "w") as zipf:
    for file in select_file:
        zipf.write(file, os.path.basename(file))

print(f"The file was compressed with success!")

window.close()
