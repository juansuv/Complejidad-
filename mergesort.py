from llenavector import llena_vector
import time
import sys

lista = [1, 3, 66, 4, 2, 6, 7, 10, 5, 2, 3, -3, 7]
lista2 = llena_vector(100000)
sys.setrecursionlimit(100000000)


def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def measure_merge():
    chuncks_low = [10, 15, 20, 25, 50, 100, 200, 500,750,1000]
    chuncks = [1000, 2000, 3000, 10000, 20000, 40000, 50000, 90000,100000]
    chuncks_high = [100000, 200000, 300000,400000,500000,600000,700000,800000,900000,1000000]
    for chunks in [chuncks_low, chuncks,chuncks_high]:
        for chunk in chunks:
            lista = llena_vector(chunk)
            inicio = time.time()
    # -------------
            mergeSort(lista)
            fin = time.time()
            print(f"{chunk},{ fin-inicio}") 
            lista[:] = []


measure_merge()
