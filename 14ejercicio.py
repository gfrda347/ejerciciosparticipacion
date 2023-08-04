#Escribir una función que calcule la media aritmética de una lista de números.
def media_aritmetica(numeros):
    if not numeros:
        return None

    suma = sum(numeros)
    media = suma / len(numeros)
    return media

def main():
    lista = [1, 2, 3, 4, 5]
    resultado = media_aritmetica(lista)
    print(f"La media aritmética de la lista {lista} es: {resultado}")

if __name__ == "__main__":
    main()
