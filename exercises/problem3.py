value = 600851475143
n = 2
populate = []

while value > 1:
    if value % n == 0:
        value //= n
        populate.append(n)
    else:
        n += 1
print(populate)
