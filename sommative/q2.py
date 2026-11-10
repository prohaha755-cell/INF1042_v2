
celsius = float(input("Entrez la temperature en Celsius : "))

if celsius < -273.15:
    print("Temperature invalide")

else:
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    print("Celsius :", round(celsius, 2))
    print("Fahrenheit :", round(fahrenheit, 2))
    print("Kelvin :", round(kelvin, 2))
