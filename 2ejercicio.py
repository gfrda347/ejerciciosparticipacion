#Escribir una función que calcule el área de un círculo dado su radio
import math

def area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    
    area = math.pi * radio ** 2
    return area

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    try:
        resultado = area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {resultado:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
