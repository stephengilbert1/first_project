def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

temp = float(input("Enter temperature in Celsius: "))
f, k = convert_temperature(temp)
print(f"Fahrenheit: {f}, Kelvin: {k}")
