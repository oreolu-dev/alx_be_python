# conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9) #for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) #for C to F

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)


def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

# main sript
try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

while True:
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if temperature_unit in ("C", "F"):
        break
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

# conversion

if temperature_unit == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature:.2f}°C is {converted_temperature:.2f}°F")
else:
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature:.2f}°F is {converted_temperature:.2f}°C")

