filenames = ["1.doc.txt", "2.report.txt", "3.presentation.txt"]

new_filename = [filename.replace(".", "-", 1) for filename in filenames]

print(new_filename)