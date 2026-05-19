


# ─────────────────────────────────────────────
# 1. MOCHILA 0/1
# Estrategia: Memoization Top-Down con diccionario
# T: O(n * W)   |   S: O(n * W)
# ─────────────────────────────────────────────
def mochila(pesos, valores, capacidad):
    """Retorna el máximo valor que cabe en la mochila."""
    memo = {}

    def dp(i, c):
        # Caso base: no hay más ítems o capacidad agotada
        if i < 0 or c == 0:
            return 0
        # Retornar resultado ya calculado
        if (i, c) in memo:
            return memo[(i, c)]

        # Decisión: no tomar el ítem i
        no_tomar = dp(i - 1, c)

        # Decisión: tomar el ítem i (solo si cabe)
        tomar = 0
        if pesos[i] <= c:
            tomar = valores[i] + dp(i - 1, c - pesos[i])

        memo[(i, c)] = max(tomar, no_tomar)
        return memo[(i, c)]

    return dp(len(pesos) - 1, capacidad)

print(mochila([1,1,1],[10,20,30],2))
    #ej [1,1,1] [10,20,30]
# ─────────────────────────────────────────────
# 2. LIS — Longest Increasing Subsequence
# Estrategia: Memoization Top-Down con diccionario
# T: O(n²)   |   S: O(n)
# ─────────────────────────────────────────────
def lis(arr):
    """Longitud de la subsecuencia creciente más larga."""
    n = len(arr)
    if n == 0:
        return 0

    memo = {}

    def dp(i, prev_idx):
        # Caso base: hemos procesado todos los elementos
        if i == n:
            return 0
        # Retornar resultado ya calculado
        if (i, prev_idx) in memo:
            return memo[(i, prev_idx)]

        # Opción 1: Saltar el elemento actual (no incluirlo)
        resultado = dp(i + 1, prev_idx)

        # Opción 2: Incluir arr[i] si es mayor al último incluido
        if prev_idx == -1 or arr[i] > arr[prev_idx]:
            incluir = 1 + dp(i + 1, i)
            resultado = max(resultado, incluir)

        memo[(i, prev_idx)] = resultado
        return resultado

    # Iniciamos sin ningún elemento previo (prev_idx = -1)
    return dp(0, -1)
print(lis([3,1,5]))

# ─────────────────────────────────────────────
# 3. DISTANCIA DE EDICIÓN (Levenshtein)
# Estrategia: Memoization Top-Down con diccionario
# T: O(m * n)   |   S: O(m * n)
# ─────────────────────────────────────────────
def distancia_edicion(s1, s2):
    """Mínimo número de operaciones para convertir s1 en s2."""
    memo = {}

    def dp(i, j):
        # Caso base: una cadena se agotó
        if i == 0:
            return j   # Insertar j caracteres restantes de s2
        if j == 0:
            return i   # Eliminar i caracteres restantes de s1

        # Retornar resultado ya calculado
        if (i, j) in memo:
            return memo[(i, j)]

        if s1[i - 1] == s2[j - 1]:
            # Caracteres iguales: sin costo adicional
            memo[(i, j)] = dp(i - 1, j - 1)
        else:
            insercion   = dp(i, j - 1)       # Insertar carácter en s1
            eliminacion = dp(i - 1, j)        # Eliminar carácter de s1
            sustitucion = dp(i - 1, j - 1)   # Sustituir carácter
            memo[(i, j)] = 1 + min(insercion, eliminacion, sustitucion)

        return memo[(i, j)]

    return dp(len(s1), len(s2))


# ─────────────────────────────────────────────
# 4. LCS — Longest Common Subsequence
# Estrategia: Memoization Top-Down con diccionario
# T: O(m * n)   |   S: O(m * n)
# ─────────────────────────────────────────────
def lcs(s1, s2):
    """Longitud de la subsecuencia común más larga."""
    memo = {}

    def dp(i, j):
        # Caso base: una cadena se agotó
        if i == 0 or j == 0:
            return 0
        # Retornar resultado ya calculado
        if (i, j) in memo:
            return memo[(i, j)]

        if s1[i - 1] == s2[j - 1]:
            # Caracteres coinciden: extender la subsecuencia
            memo[(i, j)] = 1 + dp(i - 1, j - 1)
        else:
            # Tomar el mejor de ignorar un carácter de s1 o de s2
            memo[(i, j)] = max(dp(i - 1, j), dp(i, j - 1))

        return memo[(i, j)]

    return dp(len(s1), len(s2))


# ─────────────────────────────────────────────
# 5. ROBO DE CASAS (House Robber)
# Estrategia: Memoization Top-Down con diccionario
# T: O(n)   |   S: O(n)
# ─────────────────────────────────────────────
def robo_casas(dinero):
    """Máximo dinero sin robar casas adyacentes."""
    n = len(dinero)
    if n == 0:
        return 0

    memo = {}

    def dp(i):
        # Caso base: no quedan casas
        if i >= n:
            return 0
        # Retornar resultado ya calculado
        if i in memo:       
            return memo[i]

        # Decisión: robar casa i (saltar la siguiente) o no robarla
        robar     = dinero[i] + dp(i + 2)
        no_robar  = dp(i + 1)

        memo[i] = max(robar, no_robar)
        return memo[i]

    return dp(0)

print(robo_casas[1,5,3])






