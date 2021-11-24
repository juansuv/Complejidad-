def suma(num):                       #o(n)
    suma=0                           #o(1)
    for i in range(1, num+1):        #o(n)
        suma += i                    #o(2)
    return str(suma)                 #o(1)

print(suma(3))
        #max(o(1),o(n),o(2))=o(n)
        # 1+n*1+2n+1
        #2+n+2n
        #2+3n
        #o(3n+2)
        #o(n)
