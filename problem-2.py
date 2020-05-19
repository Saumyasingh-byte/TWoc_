n = int(input("Enter the no of tuples "))
m = int(input("Enter the no of elements in each tuple "))
lst = []
for i in range(n):
    print("Enter the elements in Tuple", i + 1)
    tpl = []
    for j in range(m):
        tpl.append(int(input("Enter the element " + str(j + 1) + ": ")))
    lst.append(tuple(tpl))
N = int(input("Enter the Nth index about which you want to sort the list: "))
lst.sort(key = lambda x : x[N])
print("After sorting tuple List by Nth index sort:",lst)
