from llenavector import llena_vector
import time
import sys

lista= [1,3,66,4,2,6,7,10,5,2,3,-3,7]
lista2= llena_vector(100000)
sys.setrecursionlimit(100000000)

def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])

def measure_quicksort():
    chuncks_low=[10,15,20,25,50,100,200,500]
    chuncks = [1000,2000,3000,10000,20000,40000,50000,90000,1000000,2000000,3000000,4000000,9000000,10000000]
    for chunks in [chuncks_low,chuncks]:
        for chunk in chunks:
        
            lista=llena_vector(chunk)
            print("lleno vector",chunk)
            inicio = time.time()
    # -------------
            quicksort(lista)
            fin = time.time()
            print(f"chunk de {chunk} se demoro { fin-inicio}") 
            lista[:]=[]


measure_quicksort()