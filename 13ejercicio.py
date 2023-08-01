#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y division
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero."
    return a / b

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado_suma = suma(numero1, numero2)
resultado_resta = resta(numero1, numero2)
resultado_multiplicacion = multiplicacion(numero1, numero2)
resultado_division = division(numero1, numero2)


print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)


