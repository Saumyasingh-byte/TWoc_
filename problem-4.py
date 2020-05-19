size = int(input("Enter the no of items you want to add in Dictonary: "))
Dict = dict()
for i in range(size):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictonary: "))
    Dict[key] = value
result = dict()
for key,value in Dict.items():
    if value not in result.values():
        result[key] = value
print("Dictonary after removing duplicate values: ", result)
