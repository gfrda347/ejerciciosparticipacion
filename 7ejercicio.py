def encontrar_maximo_minimo(lista):
    if not lista:
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo

lista_dada = [2, 5, 1, 8, 3, 9, 4]
maximo, minimo = encontrar_maximo_minimo(lista_dada)

print("Número más grande:", maximo)
print("Número más pequeño:", minimo)
