def Ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ackermann(m - 1, 1)
    return Ackermann(m - 1, Ackermann(m, n - 1))
o = int(input("Enter the value of o: "))
p = int(input("Enter the value of p: "))
print("The result is", Ackermann(o,p))
