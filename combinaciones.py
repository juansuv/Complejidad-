import math

def factorial_(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def comb_1(n,m):
         return math.factorial (n) // (math.factorial (n-m) * math.factorial (m)) #Utilice la función factorial en matemáticas para calcular el número de combinaciones directamente

def comb_2(n,m):
         return factorial_ (n) // (factorial_ (n-m) * factorial_ (m)) #Utilice su propia función factorial para calcular el número de combinaciones

if __name__=='__main__':
    print(comb_1(3,2))
    print(comb_2(3,2))