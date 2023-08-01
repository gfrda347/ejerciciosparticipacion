#. Escribir un programa que determine si un número dado es par o impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero_ingresado = int(input("Ingrese un número: "))

resultado = es_par_o_impar(numero_ingresado)

print("El número", numero_ingresado, "es", resultado)
