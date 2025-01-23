a = 1
b = 2
result = 0
limit = 4000000

while b <= limit:
    if b % 2 == 0:
        result += b
    a, b = b, a + b

print(result)

# for i in range(0, 100):
#     if i % 2 == 0:
#         result += count
#         if result <= 4000000:
#             break
#
# print(count)