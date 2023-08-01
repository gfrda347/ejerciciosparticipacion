# Crear una función que invierta el orden de los elementos en una lista dada.
def invertir_lista(lista):
    return lista[::-1]

mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)
