#Crear un programa que calcule la suma de los números en una lista dada
def suma_lista(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

def main():
    lista = [1, 2, 3, 4, 5]
    resultado = suma_lista(lista)
    print(f"La suma de los números en la lista {lista} es: {resultado}")

if __name__ == "__main__":
    main()
