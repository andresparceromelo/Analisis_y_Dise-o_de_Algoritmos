def resolve_coin_change_problem(coins, x):
    if len(coins) == 0:
        return -1
    
    memo = {}

    def dp(i):
        if i == 0:
            return 0
        if i < 0:
            return float('inf')
            
        if i in memo:
            return memo[i]
            
        min_monedas = float('inf')
        for coin in coins:
            resultado = 1 + dp(i - coin)
            min_monedas = min(min_monedas, resultado)
            
        memo[i] = min_monedas
        return min_monedas

    respuesta = dp(x)
    return respuesta if respuesta != float('inf') else -1

print(resolve_coin_change_problem([1, 3, 4], 6))
