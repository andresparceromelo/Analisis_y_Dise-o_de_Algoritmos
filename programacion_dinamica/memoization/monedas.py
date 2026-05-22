def vender_varilla(v,longitud,precio):
    n = len(longitud)

    memo = {}

    def dp(i,v):
        
        if i <=0 or v == 0:
            return 0

        if i in memo:
            return memo[i]
        
        if v >= longitud[i]:
            tomar = precio[i] + dp(i, v - longitud[i])
        
        no_tomar = dp(i-1, v)
        
        memo[i] = max(no_tomar, tomar)

        return memo[i]
    return dp(n-1, v)

vender_varilla(4,[1,2,3,4],[1,5,8,9])