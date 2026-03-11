def palindromo(palabra):
    texto_limpio = palabra.replace("", "").lower()

    def verificar(izq, der):
        
        if izq >= der:
            return True
        
        if texto_limpio[izq] != texto_limpio[der]:
            return False
        return verificar( izq + 1, der - 1)
    
    return verificar(0, len(texto_limpio)-1)

prueba = palindromo("reconoce")
print(prueba)

