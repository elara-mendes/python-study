import FreeSimpleGUI as sg
import zipfile

def extract_file(file, dest_dir):
    with zipfile.ZipFile(file, 'r') as zipf:
        zipf.extractall(dest_dir)


text = sg.Text("Which file do you want to extract?")
input_label = sg.Input(key="folder"), sg.FileBrowse()
output_label = sg.Input(key="folder_dest"), sg.FolderBrowse()
button = sg.Button("Extract")
text_success = sg.Text("", text_color="Green")

window = sg.Window("Extractor", layout=[[text], [input_label], [output_label], [button, text_success]])

while True:
    events, values = window.read()

    if events == sg.WIN_CLOSED or events == 'Exit':
        break

    match events:
        case "Extract":
            extract_file(values["folder"], values["folder_dest"])
            text_success.update("File extracted with success!")
    print(events)
    print(values)