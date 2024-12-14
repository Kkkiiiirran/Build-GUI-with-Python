class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

# Creating instances of the Student class
Kiran = Student("Kiran", 20)
Kiran.display_info()

Priya = Student("Priya", 30)
Priya.display_info()
