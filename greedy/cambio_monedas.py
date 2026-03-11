# • Problema: Dar cambio con el menor número de monedas
# • Monedas disponibles: [1, 5, 10, 25] centavos
                        #  [25,10,5,1]   
# • Cantidad a devolver: 63 centavos
# • Estrategia greedy: siempre usar la moneda más grande posible
# • Solución: 25 + 25 + 10 + 1 + 1 + 1 = 6 monedas

def cambio_monedas_menor(lista_monedas: list, cantidad_devolucion: int):
        lista_monedas.sort(reverse=True)
        cambio_greedy=0
        for moneda in lista_monedas:
            if moneda <= cantidad_devolucion:
                n=cantidad_devolucion//moneda
                cantidad_devolucion -= n*moneda
                cambio_greedy += n
        if cantidad_devolucion > 0:
             return "pailangas mi apa"
        return cambio_greedy
        
    

ejemplo = cambio_monedas_menor([1,5,10], 3) 
print(ejemplo)

