with open("members.txt", "r") as file:
    members = file.readlines()

members.append("Solomon Right")

with open("members.txt", "w") as file:
    file.writelines(members)
