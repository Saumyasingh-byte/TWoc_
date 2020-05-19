s=input(" enter the string")
l=0
for x in set(s):
    l+=s.count(x)%2
if l>0:
    l-=1
print(" string will be palindromic if {}  letters are removed".format(l))
