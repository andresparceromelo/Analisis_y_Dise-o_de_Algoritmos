def resolve_coin_change_problem(coins, x):
    """
    Retorna el mínimo número de monedas necesarias para sumar la cantidad 'x'.
    Si no es posible, retorna -1.
    """
    # Manejo de casos globales
    if len(coins) == 0:
        return -1
    
    # PASO 1: Crear la memoria
    memo = {}

    # PASO 2: El "Obrero" (Estado)
    # Solo necesitamos 'c' (cantidad restante) porque podemos reusar las monedas.
    def dp(c):
        # A) Casos base
        if c == 0:
            return 0           # Misión cumplida: no necesito más monedas
        if c < 0:
            return float('inf')    # Me pasé: retorno un costo infinito para descartarlo
            
        # B) Comprobar Memoria
        if c in memo:
            return memo[c]
            
        # C) Transición: Probar todas las opciones
        min_monedas = float('inf')
        
        for coin in coins:
            # Si uso esta moneda, sumo 1 a la cuenta y pido resolver lo que sobra
            resultado = 1 + dp(c - coin)
            
            # Me quedo con la opción que use menos monedas
            min_monedas = min(min_monedas, resultado)
            
        # D) Guardar en memoria y retornar
        memo[c] = min_monedas
        return min_monedas

    # PASO 3: Disparar la primera llamada con la cantidad total
    respuesta = dp(x)
    
    # Si la respuesta es infinito, significa que ninguna combinación sirvió
    if respuesta == float('inf'):
        return -1
    return respuesta

# ─────────────────────────────────────────────
# PRUEBAS
# ─────────────────────────────────────────────
if __name__ == "__main__":
    monedas = [1, 5, 10, 25]
    
    # Prueba 1: 36 deberia ser 3 (25 + 10 + 1)
    print(f"Para sumar 36 con {monedas} necesitas: {resolve_coin_change_problem(monedas, 36)} monedas.")
    
    # Prueba 2: 11 con monedas [2, 5] deberia ser 3 (5 + 2 + 2 + 2)
    print(f"Para sumar 11 con [2, 5] necesitas: {resolve_coin_change_problem([2, 5], 11)} monedas.")
    
    # Prueba 3: Caso imposible (sumar 3 con monedas de 2)
    print(f"Para sumar 3 con [2] necesitas: {resolve_coin_change_problem([2], 3)} monedas.")