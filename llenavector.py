from random import randrange

def llena_vector(num:int):                        #o(n)
    vector=[None]*num                             #o(1)
    for i in range(0, num):                       #o(n)
        vector[i]=int(randrange(9999))            #o(n) o o(randrange)
    return vector                                 #o(1)

print(llena_vector(5))
        #max(o(1),o(n),o(2))=o(n)
        # 1+n*1+2n+1
        #2+n+2n
        #2+3n
        #o(3n+2)
        #o(n)
