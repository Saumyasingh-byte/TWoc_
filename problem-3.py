def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(" swapped values of a is {} and b is {}".format(a,b))


n=int(input(" enter the value of a"))
y=int(input(" enter the value of b"))
swap(n,y)
