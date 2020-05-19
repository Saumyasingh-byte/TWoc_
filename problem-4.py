n=int(input("Enter the no. of elements in the dictionary "))
arr=dict()
for i in range (n):
    key=int(input("Enter the key "))
    value=int(input("Enter the value "))
    arr[key]=value
result = dict()
for key,value in arr.items():
    if value not in result.values():
        result[key] = value
print("Dictonary after removing duplicates  ", result)
