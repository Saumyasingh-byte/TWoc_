def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    print(" swaped value of a is {} and b is {}".format(x,y))



a=int(input(" enter first number a: "))
b=int(input(" enter second number b : "))
print(" a={} and b={} ".format(a,b))
swap(a,b)
