#Crear un programa que genere una matriz de números y la imprima en pantalla.
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = int(input(f"Ingrese el número para la posición [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz_generada = generar_matriz(filas, columnas)

print("Matriz generada:")
imprimir_matriz(matriz_generada)
