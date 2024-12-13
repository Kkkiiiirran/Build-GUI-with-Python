class Dog:
    animal_type = "mammal"
    name = "dog"

    def fun(self):
        print(f"I am a {self.animal_type}")
        print(f"I am a {self.name}")
    

Rodger = Dog()
Rodger.fun()

Puff = Dog()
Puff.fun()
