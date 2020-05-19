def convert(num):   
    temp=num
    sum=0
    count=1
    if temp==0:
        return 5
    while temp>0:
        if temp%10==0:
            sum+=(5*count)
        count*=10
        temp=int(temp/10)
    return num+sum

num=int(input('enter the number'))
convert(num)
