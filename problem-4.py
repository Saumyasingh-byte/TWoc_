s = input("Enter the number: ")
sp = str(s)
l = len(s) - 2
Min = s[-1]
for i in range(l, -1, -1):
    u = s[i]
    if u < Min:
        s = s[:i] + Min + u + s[l:i:-1]
        break
if sp == s:
    print("Sorry! no number can be formed")
else:
    print("The next greater number is",s)
