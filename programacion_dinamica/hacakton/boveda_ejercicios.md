"""
═══════════════════════════════════════════════════════════════════════════════
                    RETO DP — ESTILO KAGGLE / COMPETENCIA
═══════════════════════════════════════════════════════════════════════════════

Implementa cada función. Luego ejecuta:

    python juez.py

El juez correrá tus soluciones contra casos de prueba ocultos con timeout.
Los casos grandes SOLO pasan si usas memorización correctamente.

Reglas del juego:
    ✓ Cada caso resuelto correctamente suma puntos
    ✗ Timeout o resultado incorrecto = 0 puntos en ese caso
    ⭐ Obtener 100% en un problema te da una estrella

¡Suerte!
"""


# ═══════════════════════════════════════════════════════════════════════════
# PROBLEMA 1: Mochila 0/1
# ═══════════════════════════════════════════════════════════════════════════
#
# Dados pesos, valores y capacidad, maximizar el valor total sin exceder
# la capacidad. Cada objeto se toma 0 o 1 vez.
#
# Ejemplo:
#   pesos = [1, 3, 4, 5], valores = [1, 4, 5, 7], capacidad = 7
#   → 9  (tomar objetos 1 y 3: pesos 3+4=7, valores 4+5=9)
#

def mochila(pesos, valores, capacidad):
    """Retorna el máximo valor que cabe en la mochila."""
    # TU CÓDIGO AQUÍ
    pass


# ═══════════════════════════════════════════════════════════════════════════
# PROBLEMA 2: Subsecuencia Creciente Más Larga (LIS)
# ═══════════════════════════════════════════════════════════════════════════
#
# Dado un arreglo, retornar la LONGITUD de la subsecuencia estrictamente
# creciente más larga.
#
# Ejemplo:
#   [10, 9, 2, 5, 3, 7, 101, 18]  → 4
#   [0, 1, 0, 3, 2, 3]            → 4
#

def lis(arr):
    """Longitud de la subsecuencia creciente más larga."""
    # TU CÓDIGO AQUÍ
    pass


# ═══════════════════════════════════════════════════════════════════════════
# PROBLEMA 3: Distancia de Edición (Levenshtein)
# ═══════════════════════════════════════════════════════════════════════════
#
# Mínimo de operaciones (insertar, eliminar, reemplazar) para convertir
# s1 en s2.
#
# Ejemplo:
#   "gato" → "pato"   = 1
#   "kitten" → "sitting" = 3
#

def distancia_edicion(s1, s2):
    """Mínimo número de operaciones para convertir s1 en s2."""
    # TU CÓDIGO AQUÍ
    pass


# ═══════════════════════════════════════════════════════════════════════════
# PROBLEMA 4: Subsecuencia Común Más Larga (LCS)
# ═══════════════════════════════════════════════════════════════════════════
#
# Longitud de la subsecuencia común más larga entre dos cadenas.
#
# Ejemplo:
#   "ABCBDAB", "BDCAB"  → 4  ("BCAB")
#   "AGGTAB", "GXTXAYB" → 4  ("GTAB")
#

def lcs(s1, s2):
    """Longitud de la subsecuencia común más larga."""
    # TU CÓDIGO AQUÍ
    pass


# ═══════════════════════════════════════════════════════════════════════════
# PROBLEMA 5: Robo de Casas
# ═══════════════════════════════════════════════════════════════════════════
#
# Arreglo con el dinero de cada casa. No se pueden robar dos casas
# adyacentes. Retornar el máximo dinero que se puede robar.
#
# Ejemplo:
#   [1, 2, 3, 1]      → 4   (casas 0 y 2)
#   [2, 7, 9, 3, 1]   → 12  (casas 0, 2, 4)
#

def robo_casas(dinero):
    """Máximo dinero sin robar casas adyacentes."""
    # TU CÓDIGO AQUÍ
    pass