get_number = int(input("Write a number:"))

if get_number <= 1:
    print("Não é primo")
elif get_number == 2:
    print(f"{get_number} é primo")
else:
    for i in range(2, int(get_number ** 0.5) + 1):
        if get_number % i == 0:
            print(f"{get_number} não é primo")
            break
    else:
        print("É primo")
