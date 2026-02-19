class Animal:
    def make_noise(self):
        print("Weeeeeeee! Animal super class")

class Dog(Animal):
    def make_noise(self):
        print("Woof woof!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()    # calls Animal super base classes make_noise() method
        print("Meow!")          # prints its sound Meow

class Rooster(Animal):
    def make_noise(self):
        print("Cock-a-doodle-doo!")

class papegoja(Animal):
    def make_noise(self):
        print("Squawk!")

def sound_off(animal_list):     # function made global, so all objects could access
     for animal in animal_list:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
p = papegoja()
sound_off([c, d, h, p])