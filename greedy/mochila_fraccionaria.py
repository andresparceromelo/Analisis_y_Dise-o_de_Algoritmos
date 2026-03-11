# • Tienes una mochila con capacidad W
# • Hay n objetos con peso y valor
# • Puedes tomar fracciones de objetos
# • Objetivo: maximizar el valor total
# • Estrategia: ordenar por valor/peso y tomar los mejores

def optimizacion_mochila(capacidad: int, objetos: list[tuple]):
    #ordenar la lista: porque lo que necesito es utilizar los elementos que mejor ratio tengan
    
    objetos = sorted(objetos,key = lambda x : x[1]/x[0], reverse = True)

    mochila=[]

    for peso,valor in objetos:
        if capacidad > peso:
            capacidad -= peso
            mochila.append((peso,valor))
            
        else:
            if capacidad > 0:
                fraccion = capacidad/peso
                capacidad -= fraccion * peso
                mochila.append((peso,valor,fraccion))
        
    return mochila
            
            
    
    



prueba = optimizacion_mochila(10, [(5,150),(2,50),(5,80),(1,1)])
print(prueba)
