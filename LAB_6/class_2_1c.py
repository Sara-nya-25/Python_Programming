"""
Add the country's area as a property to the class. Use a parameter to the constructor, i.e. the __init__ method.
Give the area a default value of None so that you don't have to specify the area when creating a country object.
Example of a default value for a common function:
# y has a default value of 10
def example(x, y=10):
print(x + y)
example(2) # prints 12
"""
class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area

    def print_info(self):
        return f"{self.__name}'s population is {self.__population:.2f} million with land area of {self.__area} Sq Km"


se = Country("Sweden", 10.5)
print(se.print_info())
no = Country("Norway", 5.5, 385207)
print(no.print_info())
"""
output:
Sweden's population is 10.50 million with land area of None Sq Km
Norway's population is 5.50 million with land area of 385207 Sq Km

"""