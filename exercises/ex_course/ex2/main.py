filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(filename, "w") as file:
        file.writelines("Hello")
