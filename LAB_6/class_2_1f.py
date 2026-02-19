"""
1f Change "print_info" so that it prints all official languages, on a new line.
"""

class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = []

    def print_info(self):
        info = f"\n{self.__name}'s population is {self.__population:.2f} million"
        if self.__area is not None:
            info += f" with area of {self.__area:.2f} sq kms"
        if self.__language:
            lang_str = ', '.join(self.__language)
            info += f"\nOfficial languages spoken are {lang_str}  "
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
Sweden's population is 10.50 million
Official languages spoken are Swedish  

Norway's population is 5.50 million with area of 385207.00 sq kms
Official languages spoken are Norwegian, Sami  
"""