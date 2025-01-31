import random

# head_or_tail = input("Write head or tail:")

# for i in range(0, 1):
#     head = random.uniform(0, 1)
#     tail = random.uniform(0, 1)
#
#     head_percentage = head * 100
#     tail_percentage = tail * 100
#
#     if head_percentage > tail_percentage:
#         print(f"Head: {head_percentage:.2f}%")
#     else:
#         print(f"Tail: {tail_percentage:.2f}%")

# head = 0
# tail = 1
#
# for i in range(1, 10):
#     random.choice([head, tail])

head = 0
tail = 0
count = 0
while count < 5:
    head_or_tail = input("Write head or tail 5 times:").lower()
    if head_or_tail == "head":
        head += 1
    elif head_or_tail == "tail":
        tail += 1
    elif head_or_tail != "tail" and head_or_tail != "head":
        print("Wrong, write head or tail!")
        continue
    count += 1

result = f"Head: {(head / 5) * 100:.1f}%, Tail: {(tail / 5) * 100:.1f}%\n"

# with open("result.txt", "r") as file:
#     file.read()

with open("result.txt", "a") as file:
    file.write(result)

print(result)


