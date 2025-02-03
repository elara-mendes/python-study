password_input = input("Write your password:")

password_validation = {
    "Uppercase": False,
    "Digit": False,
    "Length": False
}

# if any(char.isupper() for char in password_input):
#     if any(char.isdigit() for char in password_input):
#         if len(password_input) >= 8:
#             print("Strong")
# else:
#     print("Weak")

if any(char.isupper() for char in password_input):
    password_validation["Uppercase"] = True
    if any(char.isdigit() for char in password_input):
        password_validation["Digit"] = True
        if len(password_input) >= 8:
            password_validation["Length"] = True

print(password_validation)
if all(password_validation.values()):
    print("Strong pass")
else:
    print("Weak pass")

    f"""
    It's similar to ternary operator but with for-loop? /
    The professor's version is quite different, he's appending
    three True boolean values in a list, to discover if the password is 
    strong or not.
    
    all() return True or False about the multiple conditions list or something
    else. Can we concatenate with string?
    
    I'll try with dictionary too.
    all().values() get only the values from dict.
    """