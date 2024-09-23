FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temp = float(input("Enter the temperature to convert: "))
    deg = input('is this temperature in Celsius or Fahrenheit? (C/F): ')
    output = ""
    match deg:
        case "F":
            output = f"{temp}°F is {convert_to_celsius(temp)}°c"
        case "C":
            output = f"{temp}°C is {convert_to_fahrenheit(temp)}°F"
        case _:
            output =  "Invalid temperature. Please enter a numeric value."
    print(output)
# main()