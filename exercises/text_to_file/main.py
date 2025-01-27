text = ["rice", "potato", "naruto"]

filenames = ["file1.txt", "file2.txt", "file3.txt"]

for filename, content in zip(filenames, text):
    with open(filename, "w") as file:
        file.writelines(content)
