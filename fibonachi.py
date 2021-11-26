def fib(n):
    if n == 0:                      #o(1)
        return 0                    #o(1)
    if n == 1:                      #o(1)
        return 1                    #o(1)
    return fib(n-1) + fib(n-2)      #o(6n+6n)

print(fib(10))

    #  1  n=1 o n=2 
    #  t(n-1)+t(n-2)  n>2

    # t(n-1)+t(n-2)  <= 2*t(n-1)
    #  t(n) = 2*t(n-1)
    #  t(n-1) = 2*t(n-2)
    #  t(n-2) = 2*t(n-3)
    #  t(n-3) = 2*t(n-4)
    #  t(n) = 2•t(n-1)+2•2•t(n-2)+2•2•2•t(n-3)++2•2•2•2•t(n-4)
    # sum 2^i•t(n-i)
    # 2^n•t(n)
    # o(2^n)
    