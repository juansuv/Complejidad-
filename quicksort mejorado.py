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
    chuncks = [1000,10000,100000,1000000,5000000,9000000,10000000,100000000,1000000000,10000000000]
    for chunk in chuncks:
        
        lista=llena_vector(chunk)
        print("lleno vector",chunk)
        inicio = time.time()
# -------------
        quicksort(lista)
        fin = time.time()
        print(f"chunk de {chunk} se demoro { fin-inicio}") 
        lista[:]=[]


measure_quicksort()