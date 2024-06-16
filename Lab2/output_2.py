class Phone:
    def __init__(self, code, number):
        self.code = code
        self.number = number

    def full_number(self):
        return f"{self.code}{self.number}"

class UserType:
    ENGINEER = 1
    MANAGER = 2    

class User:
    def __init__(self, name, age, user_type, phone):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.phone.full_number())

# Приклад використання класу
phone = Phone("050", "9379992")
user = User("John", 25, UserType.ENGINEER, phone)
user.print_details()
