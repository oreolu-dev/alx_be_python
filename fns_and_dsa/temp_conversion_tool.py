# conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Temperature must be a number.")
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number.")
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def get_temperature_input():
    try:
        return float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_temperature_unit():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ("C", "F"):
            return unit
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")

# main script
try:
    temperature = get_temperature_input()
    unit = get_temperature_unit()

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {converted:.2f}°F")
    else:
        converted = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {converted:.2f}°C")

except ValueError as e:
    print(e)
