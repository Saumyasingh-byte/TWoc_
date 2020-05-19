def fibonacci(n):
    c=0
    d=1
    b=c+d
    print(c)
    print(d)
    print(b)
    while b<n:
        c,d=d,b
        b=c+d
        if b<n:
            print(b)


fibonacci(100)
