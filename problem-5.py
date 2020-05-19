def Sum(n) : 

    if (n <= 0) : 

        return 0

    fibo =[0] * (n+1) 

    fibo[1] = 1

    s = fibo[0] + fibo[1] 

    for i in range(2,n+1) : 

        fibo[i] = fibo[i-1] + fibo[i-2] 

        s = s + fibo[i] 

    return s 

n = 4

print("Sum of Fibonacci numbers is : " , Sum(n)) 
