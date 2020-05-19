size = int(input("Enter the size of the array: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element " + str(i + 1) + " in the array: ")))
index1 = List.index(min(List))
index2 = List.index(max(List))
List1 = List[index1:] + List[:index1]
List2 = List[index2:] + List[:index2]
if List1 == sorted(List) or List2 == sorted(List, reverse = True):
    print("Array is sorted and rotated.")
else:
    print("Array is not sorted and rotated.")
