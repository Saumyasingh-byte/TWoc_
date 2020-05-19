def Merge(merge, List):
    mergedList = []
    a = 0
    b = 0
    while a != len(merge) and b != len(List[0]):
        if merge[a] < List[0][b]:
            mergedList.append(merge[a])
            a += 1
        else:
            mergedList.append(List[0][b])
            b += 1
    if a == len(merge):
        mergedList.extend(List[0][b:])
    elif b == len(List[0]):
        mergedList.extend(merge[a:])
    if len(List) == 1:
        return mergedList
    return Merge(mergedList,List[1:])

size = int(input("Enter the number of sorted lists you want to merge: "))
List= []
for i in range(size):
    List.append(list(map(int,input("Enter the elements seprated by space for sorted list number " + str(i + 1) + ": ").strip().split(" "))))
print(List)
print("The sorted list is: ", Merge(List[0],List[1:]))
