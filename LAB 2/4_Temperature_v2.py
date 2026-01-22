"""
Temperature conversion
Ask option from user to convert Celsius to Fahrenheit or Fahrenheit to celsius
"""
print("\n************* TEMPERATURE CONVERSION *************")
print("\nDo you want to enter temperature in Celcius or Fahrenheit?")
option_temperature = input(" Enter ( °C or °F): ")

if option_temperature == "C" or option_temperature == "c":
    celsius = float(input("\nEnter a temperature in degrees Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"\n {celsius} °C Celsius is {fahrenheit:.2f} °F  Fahrenheit")
elif option_temperature == "F" or option_temperature == "f":
    fahrenheit = float(input("\nEnter a temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"\n {fahrenheit} °F is {celsius:.2f} °C Celsius")
else:
    print("\nInvalid input. Please enter a valid input.")