from llenavector import llena_vector
import time
import sys

lista= [1,3,66,4,2,6,7,10,5,2,3,-3,7]
lista2= llena_vector(100000)
sys.setrecursionlimit(100000000)


def burbuja(lista):
    cont=0
    ordenado=False
    tamano=len(lista)
    comparaciones=tamano
    for _ in range(0,tamano):
        if ordenado==True:
            break
        for j in range(0,comparaciones-1):
            ordenado=True
            cont=cont+1
            if lista[j]>lista[j+1]:
                ordenado=False
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
        comparaciones=comparaciones-1
    return lista




def measure_burbuja():
    chuncks_low = [10, 15, 20, 25, 50, 100, 200, 500,750,1000]
    chuncks = [1000, 2000, 3000, 10000, 20000, 40000, 50000, 90000,100000]
    chuncks_high = [100000, 200000, 300000,400000,500000,600000,700000,800000,900000,1000000]
    for chunks in [chuncks_low, chuncks,chuncks_high]:
        for chunk in chunks:
        
            lista=llena_vector(chunk)
            inicio = time.time()
    # -------------
            burbuja(lista)
            fin = time.time()
            print(f"{chunk},{ fin-inicio}") 
            lista[:]=[]



measure_burbuja()   