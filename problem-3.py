n=int(input("Enter the no. of elements in the dictionary "))
arr=dict()
for i in range (n):
    k=int(input("Enter the key "))
    v=int(input("Enter the value "))
    arr[k]=v
print"The second largest value in the dictionary is ",(list(sorted(arr.v()))[-2])
