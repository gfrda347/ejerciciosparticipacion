#Escribir una función que calcule el factorial de un número dado.
def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

resultado_factorial = factorial(numero_ingresado)

print("El factorial de", numero_ingresado, "es:", resultado_factorial)
