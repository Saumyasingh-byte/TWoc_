size = int(input("Enter the no of words you want to add in dictonary: "))
Dict = []
for i in range(size):
    Dict.append(input("Enter the word " + str(i + 1) + ": "))
size = int(input("Enter the no of character you want to add in array: "))
array = []
result = []
print("Enter the characters in array one by one ")
for i in range(size):
    array.append(input())
for word in Dict: 
    if set(word).issubset(set(array)):
        result.append(word)
print(", ".join(result) + ".")
