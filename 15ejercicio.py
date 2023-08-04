#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

def main():
    texto = input("Ingrese una cadena de texto: ")
    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()
