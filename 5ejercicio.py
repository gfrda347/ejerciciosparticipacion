#Crear una función que convierta grados Fahrenheit a grados Celsius.
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    grados_fahrenheit = 68
    grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
    print(f"{grados_fahrenheit} grados Fahrenheit equivalen a {grados_celsius:.2f} grados Celsius.")

if __name__ == "__main__":
    main()
