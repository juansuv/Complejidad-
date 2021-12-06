from llenavector import llena_vector
import time
import sys

lista= [1,3,66,4,2,6,7,10,5,2,3,-3,7]
lista2= llena_vector(100000)
sys.setrecursionlimit(100000000)


def burbuja(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista

def measure_burbuja():
    chuncks = [1000,10000,100000,500000,900000]
    for chunk in chuncks:
        
        lista=llena_vector(chunk)
        print("lleno vector",chunk)
        inicio = time.time()
# -------------
        burbuja(lista)
        fin = time.time()
        print(f"chunk de {chunk} se demoro en burbuja {fin-inicio}") 
        lista[:]=[]


measure_burbuja()