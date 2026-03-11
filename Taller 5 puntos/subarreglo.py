# EJERCICIO 2: Subarreglo de suma máxima
# ─────────────────────────────────────────────────────────────────────────────
# Dado un arreglo de enteros (puede tener negativos), encontrar el subarreglo
# contiguo con la suma más grande. Retornar la suma.
#
# Ejemplo:
#   entrada: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   salida: 6 (el subarreglo [4, -1, 2, 1] tiene suma 6)
#

def suma_maxima_subarreglo(arr):
    max_actual=max_global=arr[0]

    for x in arr[1:]:
        max_actual=max(x,max_actual+x)
        
        

        if max_actual > max_global:
            max_global = max_actual
        
        
    return max_global

print(suma_maxima_subarreglo([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


    