alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

code_or_decode = input("Do you want to code or decode?")
message = input("Write your message:").upper()
shift = int(input("Write a number:"))

word = ""
if code_or_decode == "code":
    for letter in message:
        if letter in alphabet:
            get_index = alphabet.index(letter)
            new_index = get_index + shift
            word += alphabet[new_index % 26] # Didn't know about this
    print(word)

elif code_or_decode == "decode":
    for letter in message:
        if letter in alphabet:
            get_index = alphabet.index(letter)
            new_index = get_index - shift
            word += alphabet[new_index % 26]
    print(word)

# for letter in alphabet:
#     if message in alphabet:
#         text = alphabet.index(letter)
#         if shift >= 0:
#             number = numbers.index(shift)
#             if text == number:
#                 text = number
#                 print(text, number)


# number_index = numbers.index(shift)
# print(number_index)
# print(alphabet[number_index])