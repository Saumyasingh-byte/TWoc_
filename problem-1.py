n=int(input("Enter the no. of elements in the tuple "))
print("Enter the elements of tuple ")
arr=[]
for i in range (n):
    arr.append(input())
arr=tuple(arr)
ele=input("Enter the element whose count you wish to know ")
print(ele,"occurs ",arr.count(ele)," times")
