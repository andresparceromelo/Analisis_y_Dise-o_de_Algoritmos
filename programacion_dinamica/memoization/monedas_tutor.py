def vender_varilla(v,longitud,precio):
    n = len(longitud) 

    memo = {}

    def dp(i,v):
        
        if i == n or v == 0:
            return 0

        if (i,v) in memo:
            return memo[(i,v)]
        
        no_tomar = dp(i+1, v)
        
        tomar = 0
        if v >= longitud[i]:
            tomar = precio[i] + dp(i, v - longitud[i])
        
        
        
        memo[(i,v)] = max(no_tomar, tomar)

        return memo[(i,v)]
    return dp(0, v)

print(vender_varilla(4,[1,2,3,4],[1,5,8,9]))