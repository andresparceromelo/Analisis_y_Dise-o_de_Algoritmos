# EJERCICIO 1: Elemento mayoritario

# Dado un arreglo de enteros, encontrar el elemento que aparece mas de n/2 veces.
# Se garantiza que siempre existe un elemento mayoritario.

# Ejemplo:
#entrada: [3, 3, 4, 2, 3, 3, 5, 3, 3]

#lista = [3,3,3,3,3,3, 3 ,3,4,4,4,4,5,5,5]
#lista_mitad = len(lista)//2
#print(lista[lista_mitad])

#salida: 3 (aparece 6 veces, n/2 = 4.5)


#entrada: [3, 3, 4, 2, 3, 3, 5, 3, 3]

def contar_frecuencias(arr):
    mitad = len(arr)//2
    conteo = {}
    for x in arr:
        conteo[x] = conteo.get(x, 0) + 1
    
    return conteo

print(contar_frecuencias([3, 3, 4, 2, 3, 3, 5, 3, 3]))



