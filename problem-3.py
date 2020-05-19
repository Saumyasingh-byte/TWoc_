size = int(input("Enter the number of elements you want to add in the list: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i + 1) + ": ")))
number = 1
while True:
    if number not in List:
        break
    number += 1
print("The smallest positive number missing from the List is",number)
