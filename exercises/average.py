def average():
    with open("average.txt", "r") as file:
        temperatures = file.readlines()
        average_local = [int(i.strip()) for i in temperatures if i.strip().isdigit()]
        result = sum(average_local) / len(average_local)
        return result

print(average()) # Done

def get_maximum():
    celsius_degree = [14, 15.1, 12.3]
    maximum = max(celsius_degree)
    return maximum

celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit) # Solved