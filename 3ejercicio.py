#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

def generar_lista_numeros_aleatorios(cantidad_numeros, rango_menor, rango_mayor):
    lista_numeros = [random.randint(rango_menor, rango_mayor) for _ in range(cantidad_numeros)]
    return lista_numeros
cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))

rango_menor = int(input("Ingrese el límite inferior del rango: "))
rango_mayor = int(input("Ingrese el límite superior del rango: "))

lista_numeros_aleatorios = generar_lista_numeros_aleatorios(cantidad_numeros, rango_menor, rango_mayor)

print("Lista de números aleatorios:", lista_numeros_aleatorios)
