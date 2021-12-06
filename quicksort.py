from llenavector import llena_vector
import time
import sys

lista= [1,3,66,4,2,6,7,10,5,2,3,-3,7]
lista2= llena_vector(100000)
sys.setrecursionlimit(100000000)
def particion(lista):
    pivote = lista[0]
    menores =[]
    mayores =[]

    for i in range(1,len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    
    return menores , pivote , mayores


def quicksort(lista):
    if len(lista)<2:
        return lista
    
    menores,pivote,mayores=particion(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)


def measure_quicksort():
    chuncks = [1000,10000,100000,500000,900000]
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