
def convertir_celsius_a_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

if __name__ == "__main__":
    temp_celsius = float(input("Celcius a Fahrenheit "))

    temp_fahrenheit = convertir_celsius_a_fahrenheit(temp_celsius)
    print("La temperatura en Fahrenheit es ", temp_fahrenheit)
