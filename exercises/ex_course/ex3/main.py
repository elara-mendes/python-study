files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    with open(file, "r") as text_char:
        text = text_char.read()
        print(text)