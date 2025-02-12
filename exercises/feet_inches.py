feet_inches = input("What's the feet and inches? ")

def convert_to_meters(meters_value):
    feet_value = float(feet_inches[0])
    inches_value = float(feet_inches[2:3])
    meters_value = (feet_value * 0.3048) + (inches_value * 0.0254)
    return f"The feet is {feet_value}, the inches is {inches_value} and the result in meters is {round(meters_value, 2)}.", meters_value

result = convert_to_meters(feet_inches)

if result[1] > 0:
    print(result[0])
else:
    print("Write a correct answer.")

"""
My teacher used split to get just two elements.
"""