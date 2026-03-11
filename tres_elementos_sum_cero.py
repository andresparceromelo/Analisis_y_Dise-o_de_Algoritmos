
# EJERCICIO 3: Tres elementos que sumen cero
# ─────────────────────────────────────────────────────────────────────────────
# Dado un arreglo de enteros, determinar si existen tres elementos distintos
# (por posición) cuya suma sea exactamente 0. Retornar True/False.
#
# Ejemplo:
#   entrada: [-1, 0, 1, 2, -1, -4]
#   salida: True (porque -1 + 0 + 1 = 0)
#
def tres_suman_cero(arr):
    complementos=set()
    for x in range(len(arr)-1):
        print(-arr[x+1])
        if (-arr[x+1]) in complementos :
            return True
        complementos.add(arr[x]+arr[x+1])
        print(complementos)
    return False
        



print(tres_suman_cero([[-1, 10, 0, 5, 1] ]))