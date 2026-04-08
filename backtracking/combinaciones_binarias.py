def combinaciones_binarias(n: int):
    soluciones = []
    binario = [0,1]
    def backtrack(respuesta_actual):
        #caso base
        if len(solucion) == n:
            soluciones.append(respuesta_actual)

        