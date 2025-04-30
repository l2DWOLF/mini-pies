
# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Animal's Sound"

# Behavior Class
class Driver:
    def drive(self):
        return "Driving"
class Pilot:
    def fly(self):
        return "Flying"
    
# Cat Class
class Cat(Animal, Driver):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Meow"
# Dog Class
class Dog(Animal, Pilot):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof"
    
# App
cat1 = Cat("Ginger", "Siamese")
dog1 = Dog("Ray", "Pincher")
print(cat1.make_sound(), cat1.drive())
print(dog1.make_sound(), dog1.fly())