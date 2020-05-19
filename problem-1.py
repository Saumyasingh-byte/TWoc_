def oddoreven(n):
    n=int(n)
    if n%2==0:
        print(" even")
    else:
        print(" odd ")

def prime(n):
   p=2
   l=n//2
   while l>=a:
       if n%a==0:
            print(" not prime")
        a+=1
        l=n//a  
    print(" prime ")
       


def palindrome(n):
    m=n[::-1]
    if (m==n):
        print(" palindrome ")
    else :
        print(" not palindrome ")
        
        
def armstrong(n):
    m=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(" is armstrong")
    print(" is not armstrong")

n=input(" enter the number")
oddoreven(n)
prime(n)
palindrome(n)
armstrong(n)
