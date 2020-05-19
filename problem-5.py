n=int(input("enter the number of elements in a list1"))
lis1=[]
lis=[]
for i in range(0,n):
    lis1.append(int(input("enter the list elements")))
print(lis1)
n=int(input("enter the number of elements in a list2"))
lis2=[]
for i in range(0,n):
    lis2.append(int(input("enter the list elements")))
print(lis2)

lis=[values for values in lis1 if values in lis2]
print(lis)
