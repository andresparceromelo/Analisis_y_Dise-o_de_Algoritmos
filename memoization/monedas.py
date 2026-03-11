monedas = [1, 5, 10, 25]

def cambio_monedas(cantidad,monedas, memo = {}):
    if cantidad in memo:
        return memo[cantidad]
    
    if cantidad == 0:
        return 0

    