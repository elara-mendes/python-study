# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for number in numbers]
# print(numbers)

# def speed(distance, time):
#     return distance / time
#
# print(speed(200, 4))
#
#
# def speed(distance, time):
#     return distance / time
#
# print(speed(300, 5))

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100) # Solved
print(time)