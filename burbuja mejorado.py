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
    chuncks_low=[10,15,20,25,50,100,200,500]
    chuncks = [1000,2000,3000,10000,20000,40000,50000,90000,1000000,2000000,3000000,4000000,9000000,10000000]
    for chunks in [chuncks_low,chuncks]:
        for chunk in chunks:
        
            lista=llena_vector(chunk)
            print("lleno vector",chunk)
            inicio = time.time()
    # -------------
            burbuja(lista)
            fin = time.time()
            print(f"chunk de {chunk} se demoro en burbuja {fin-inicio}") 
            lista[:]=[]
            


measure_burbuja() 