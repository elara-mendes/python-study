import FreeSimpleGUI as sg

def convert_to_meters(feet_value, inches_value):
    meters_value = (feet_value * 0.3048) + (inches_value * 0.0254)
    return f"{round(meters_value, 2)}"


sg.theme("Black")

text = sg.Text("Convert feet/inches to m!")
feet_label = sg.Input(key="feet"),
inches_label = sg.Input(key="inches"),
button = sg.Button('Convert')
text_m = sg.Text("")
exit_button = sg.Button("Exit")

# Create the window
window = sg.Window('Convertor', layout=[[text], [feet_label], [inches_label], [button, exit_button, text_m]])

while True:
    events, values = window.read()

    if events == "Convert":
        text_m.update((convert_to_meters(float(values["feet"]), float(values["inches"]))))
        # sg.popup(convert_to_meters(float(values["feet"]), float(values["inches"])))

    if events == sg.WIN_CLOSED or events == 'Exit':
        break