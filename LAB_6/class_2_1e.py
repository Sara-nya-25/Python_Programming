"""
1e Create a new method called "add_language". It will add one of the country's official languages.
(Sweden only has one, but Finland has two languages (Swedish and Finnish) and Switzerland has four.)
To be able to save a varying number, you need to use a list.
"""

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = []

    def print_info(self):
        info = f"{self.__name}'s population is {self.__population:.2f} million"
        if self.__area is not None:
            info += f" with area of {self.__area:.2f} sq kms"
        if self.__language:
            lang_str = ', '.join(self.__language)
            info += f" and Languages spoken are {lang_str}  "
        return info

    def add_language(self, language):
        for i in language:
            self.__language.append(i)
        return self

se = Country("Sweden", 10.5)
no = Country("Norway", 5.5, 385207)
se.add_language(["Swedish"])
print(se.print_info())
no.add_language(["Norwegian","Sami"])
print(no.print_info())

"""
output:
Sweden's population is 10.50 million and Languages spoken are Swedish  
Norway's population is 5.50 million with area of 385207.00 sq kms and Languages spoken are Norwegian, Sami  

"""