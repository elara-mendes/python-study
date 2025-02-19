import FreeSimpleGUI as sg

def convert_to_meters(feet_value, inches_value):
    meters_value = (feet_value * 0.3048) + (inches_value * 0.0254)
    return f"The feet is {feet_value}, the inches is {inches_value} and the result in meters is {round(meters_value, 2)}."


text = sg.Text("Convert feet/inches to m!")
feet_label = sg.Input(key="feet"),
inches_label = sg.Input(key="inches"),
button = sg.Button('Convert')

# Create the window
window = sg.Window('Convertor', layout=[[text], [feet_label], [inches_label], [button]])

events, values = window.read()

sg.popup(convert_to_meters(float(values["feet"]), float(values["inches"])))