def primo(num):             #o(n)
    if num == 1:            #o(1)
        return False        #o(1)
    elif num == 2:          #o(1)
        return True         #o(1)
    else:                   #o(1)
        for i in range(2, num):     #o(n)
            if num % i == 0:        #o(1)
                return False        #o(1)
        
        return True                 ##o(1)

print(primo(12))
        #max(o(1),o(n),o(1))=o(n)
        # 1+1+1+1+1+n*1+2n+1
        #6+n+2n
        #6+3n
        #o(3n+6)
        #o(n)
