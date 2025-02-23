persons2 = {"first name": ["john", "laura", "sim"],
            "last name": ["smith", "eager", "age"],
            "age": [40, 45, 42]}

for i, j, k in zip(persons2["first name"], persons2["last name"], persons2["age"]):
    print(f"{i} {j}, {k}")

