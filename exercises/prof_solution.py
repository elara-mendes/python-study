while True:
    # Lendo os valores já armazenados
    with open("result.txt", "r") as file:
        sides = file.readlines()

    head_or_tail = input("Write head or tail (or type 'exit' to stop): ").lower()

    # Verificando entrada válida
    if head_or_tail == "exit":
        break
    elif head_or_tail not in ["head", "tail"]:
        print("Wrong input! Write 'head' or 'tail'.")
        continue

    # Salvando a jogada no arquivo
    with open("result.txt", "a") as file:
        file.write(head_or_tail + "\n")

    # Recontando "head" no arquivo
    nr_heads = sides.count("head\n") + (1 if head_or_tail == "head" else 0)
    total_plays = len(sides) + 1

    # Calculando porcentagem
    percentage = (nr_heads / total_plays) * 100
    print(f"Heads: {percentage:.1f}%")

# From ChatGPT

while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")

# His solution
