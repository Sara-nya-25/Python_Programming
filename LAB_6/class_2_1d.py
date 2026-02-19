#Change the "print_info" method so that it prints the area as well, but only if the area is not None.

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area

    def print_info(self):
        info = f"{self.__name}'s population is {self.__population:.2f} million"
        if self.__area is not None:

            info += f" with area of {self.__area:.2f} sq kms"
        return info

se = Country("Sweden", 10.5)
print(se.print_info())
no = Country("Norway", 5.5, 385207)
print(no.print_info())

"""
output:
Sweden's population is 10.50 million
Norway's population is 5.50 million with area of 385207.00 sq kms

"""

