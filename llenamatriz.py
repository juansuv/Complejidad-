from random import randrange

def llena_matriz(fil:int, col:int):            #o(n)      
    matriz = [[None] * col for i in range(fil)]            #o(n)
    for i in range(0, fil):                                                #o(n)*o(m) 
        for j in range(0,col):                                             #o(m)
            matriz[i][j]=int(randrange(9999))                              #o(n) o o(randrange)
    return matriz                                                          #o(1)

print(llena_matriz(5,4))

        #max(o(n),o(n)*o(m),o(n),o(1))=o(n^2)
        # n+n*m+2n+1
        #n*m+n+2n+1
        #n^2+3n+1
        #o(n^2+3n+1)
        #o(n^2)
