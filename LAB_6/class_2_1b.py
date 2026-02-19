"""
Add a method called "print_info". If you call it for the Sweden object, it should print:
"There are 10.5 million inhabitants in Sweden".
Methods should use the properties of the class, so that it works for the other countries and not just for Sweden.
"""
class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

    def print_info(self):
        return f"{self.__name}'s population is {self.__population:.2f} million"


se = Country("Sweden", 10.5)
print(se.print_info())
no = Country("Norway", 5.5)
print(no.print_info())
"""
output:
Sweden's population is 10.50 million
Norway's population is 5.50 million

"""