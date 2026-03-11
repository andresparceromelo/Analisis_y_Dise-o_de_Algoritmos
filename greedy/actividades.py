lista_de_actividades = [(7,9),(9,12),(8,10),(10,12),(6,8)]
#[(6, 8), (7, 9), (8, 10), (9, 12), (10, 12)]

def optimizador_actividades(actividades):
    actividades_ordenadas = sorted(actividades, key = lambda x : x[1])
    lista_greedy=[actividades_ordenadas[0]]
    for i in range (1,len(actividades)):
        
        if lista_greedy[-1][1] <= actividades_ordenadas[i][0]:
            
            lista_greedy.append((actividades_ordenadas[i]))

    
    return lista_greedy


prueba = optimizador_actividades(lista_de_actividades)
print(prueba)
