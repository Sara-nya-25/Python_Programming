"""
1a Iceland has 383,726 inhabitants and Denmark has 5,961,249.
Create objects for the countries. (Data from January 2024. Round off the population.)
"""
class Country:
    def __init__(self, name, pop):      # used to initialize values to a class
        self.__name = name
        self.__population = (pop / 1000000)

    def __str__(self):          # dunder method used by developers to print the values of instance
        return f"{self.__name}'s population is {self.__population:.2f} million"

ice = Country("Iceland", 383726)
print(ice)
den = Country("Denmark", 5961249)
print(den)
"""
output:
Iceland's population is 0.38 million
Denmark's population is 5.96 million

"""