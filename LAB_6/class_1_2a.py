# What does the following code do? Fix any errors.
"""
class Animal:
    def make_noise(self):
        print("We don't have a sound for this animal.")

class Dog(Animal):
    def make_noise(self):
        print("Wow!")

class Cat(Animal):
    def make_noise(shelf):      # 'shelf' -It is not error but always using 'self' is best practice self represents instance of the class, the object by itself.
        super().make_noise()
        print("Meow!")

    def sound_off(animal):
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()   # class Rooster is missing it will throw a NameError: name 'Rooster' not defined
sound_off([c, d, h]) # function inside Cat class not global and expects animal class instance
"""
# Modified code to remove the errors
class Animal:
    def make_noise(self):
        print("We don't have a sound for this animal.")

class Dog(Animal):
    def make_noise(self):
        print("Woof!")

class Cat(Animal):
    def make_noise(self):      # 'shelf' changed to 'self' as it is the best practice
        super().make_noise()    # calls Animal super base classes make_noise() method
        print("Meow!")          # prints its sound Meow

class Rooster(Animal):
    def make_noise(self):
        print("Cock-a-doodle-doo!")

def sound_off(animal_list):     # function made global, so all objects could access
     for animal in animal_list:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()   # class Rooster is missing it will throw a NameError: name 'Rooster' not defined
sound_off([c, d, h])