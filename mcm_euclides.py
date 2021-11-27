def maximo_comun_divisor(a, b):
    temporal = 0                 #o(1)
    while b != 0:                #o(n)
        temporal = b            #o(1)
        b = a % b               #o(1)
        a = temporal            #o(1)
    return a                    #o(1)


def minimo_comun_multiplo(a, b):                    #o(n)
    return (a * b) / maximo_comun_divisor(a, b)     #o(n)


a = 20
b = 6
mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")

#max(o(n),o(n)* o(n),o(1))= o(n^2)
        #n+n*n+1
        #n^2+n+1
        #o(n^2+n+1)
        #o(n^2)
