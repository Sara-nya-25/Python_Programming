"""
Temperature conversion
Ask option from user to convert Celsius to Fahrenheit or Fahrenheit to celsius
Check if temperature below 10 Or above 20 and provide clothing suggestions
"""
print("\n************* TEMPERATURE CONVERSION *************")
print("\nDo you want to enter temperature in Celcius or Fahrenheit?")
option_temperature = input(" Enter ( C or F): ")

if option_temperature == "C" or option_temperature == "c":
    celsius = float(input("\nEnter a temperature in degrees Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"\n Temperature is {fahrenheit:.2f} °F  Fahrenheit")
    if int(celsius) < 10:
        print("\n Temperature is below 10 °C. Gear Up for Winter!!")
    elif int(celsius) > 20:
        print("\n Temperature is above 20 °C. Enjoy Sunny day!! Pack your swim wear.")
elif option_temperature == "F" or option_temperature == "f":
    fahrenheit = float(input("\nEnter a temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"\n Temperature is {celsius:.2f} °C Celsius")
    if int(celsius) < 10:
        print("\n Temperature is below 10 °C. Gear Up for Winter!!")
    elif int(celsius) > 20:
        print("\n Temperature is above 20 °C. Enjoy Sunny day!! Pack your swim wear.")
else:
    print("\nInvalid input. Please enter a valid input.")
"""
Tesr Input  Expected Output
° Celsius   ° Fahrenheit
----------------------------
0              32
-17.777…       0
37.777…        100
100            212
"""
