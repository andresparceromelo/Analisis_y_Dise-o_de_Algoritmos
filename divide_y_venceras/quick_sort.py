def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivote = arr[0]
    menores = [x for x in arr[1: ] if x <= pivote]
    mayores = [x for x in arr[1: ] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)

    test = quick_sort([5,10,4,1,3,7])