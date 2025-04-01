class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.capitalize()

    def age(self, current_year):
        age = current_year - self.birthyear
        return age

user = User("elara", 1999)
print(user.age(2025))
print(user.get_name())