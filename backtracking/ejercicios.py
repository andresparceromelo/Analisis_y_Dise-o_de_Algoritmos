def subconjuntos(nums:list[int]):
    resultado=[]

    def backtrack(inicio, actual):
        resultado.append(actual[:])

        for i in range(inicio, len(nums)):
            actual.append(nums[i])
            backtrack(i + 1, actual)
            actual.pop()

    backtrack(0,[])
    return resultado


# nums= [1,2,3,4,5,6,7,8,9,10]
# prueba= subconjuntos(nums)
# print(prueba)


def subconjuntos_k(nums:list[int],k:int)->list[list[int]]:
    resultado=[]

    def backtrack(inicio, actual):

        if len(actual) == k:
            resultado.append(actual[:])
            return

        for i in range(inicio, len(nums)):
            actual.append(nums[i])
            backtrack(i + 1, actual)
            actual.pop()

    backtrack(0,[])
    return resultado

nums_2= [1,2,3,4,5,6,7,8,9,10]
prueba= subconjuntos_k(nums_2,2)
# print(prueba)




def objetivo_backtrack(nums:list[int],objetivo:int)->list[int]:
    resultado=[]
    nums.sort()

    def backtrack(inicio, actual):


        if sum(actual)==objetivo:
            resultado.append(actual[:])
            return
        
        for i in range(inicio,len(nums)):
            if (sum(actual) + nums[i]) > objetivo:
                break

            actual.append(nums[i])
            backtrack(i,actual)               #Si quiero que no se repitan numeros pongo i+1, si quiero que se repitan numeros pongo i
            actual.pop()


    backtrack(0,[])
    return resultado


# prueba=[1,3,7,2,4]
# print(objetivo_backtrack(prueba,7))



def parentesis_backtrack(n: int)->list[str]:
    resultado=[]

    def backtrack(actual, abiertos , cerrados):

        if len(actual) == 2*n:
            resultado.append(actual)
            return
        
        if abiertos < n:
            backtrack(actual + "(" ,abiertos + 1, cerrados)

        if cerrados < abiertos:
            backtrack(actual + ")", abiertos , cerrados + 1)

    backtrack("",0,0)
    return resultado

print(parentesis_backtrack(4))



