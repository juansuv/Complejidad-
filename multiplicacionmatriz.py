from random import randrange
from llenamatriz import llena_matriz

"""
X = [[12,7,3],         # o(1)
    [4 ,5,6],           
    [7 ,8,9]]
Y = [[5,8,1,2],         # o(1)  
    [6,7,3,0],
    [4,5,9,1]]
"""    
X = llena_matriz(3,3)    # o(n^2)
Y = llena_matriz(3,4)    # o(n^2)

# 3x4 matrix


def mult_matriz(X,Y):   
    result = [[0] * len(Y[0]) for i in range(len(X))]           #o(n^2)
    for i in range(len(X)):                                     # o(ñ) * o(n) * o(m)
        for j in range(len(Y[0])):                              # o(n)
            for k in range(len(Y)):                             # o(m)
                result[i][j] += X[i][k] * Y[k][j]               # o(1) 
    return result                                               # o(1)


print(mult_matriz(X,Y))

 #max(o(n^2),o(n),o(1),o(n^3))=o(n^3)
 # 3n^2 + 2(n*m*ñ) + 2
 