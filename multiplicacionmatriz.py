from random import randrange
from llenamatriz import llena_matriz

"""
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
"""    
X = llena_matriz(3,3)
Y = llena_matriz(3,4)

# 3x4 matrix


def mult_matriz(X,Y):   
    result = [[0] * len(Y[0]) for i in range(len(X))]     
    for i in range(len(X)):    
        for j in range(len(Y[0])):            
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]    
    return result


print(mult_matriz(X,Y))
