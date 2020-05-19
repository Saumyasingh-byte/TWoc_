n=int(input("Enter the no. of houses: "))
lst=[]
print("Enter the value of the houses ")
for i in range (n):
    ele=int(input())
    lst.append(ele)
x=lst[0]
if(n==1):
    print(x)
y=max(lst[0],lst[1])
if(n==2):
    print(y)
m=None
for i in range (2,n):
    m=max(lst[i]+x,y)
    x=y
    y=m
print(m)
