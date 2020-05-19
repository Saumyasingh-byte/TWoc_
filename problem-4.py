n=int(input("enter the number of elements in a list"))
lis=[]
for i in range(0,n):
    lis.append(int(input("enter the list elements")))
print(lis)

f=list(set(lis))
print(f)
