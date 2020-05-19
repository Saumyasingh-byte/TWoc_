def greatest(arr):
    n=len(arr)
    maxi=arr[n-1]
    arr[n-1]=-1
    for i in range(n-2,-1,-1):
        temp=arr[i]
        arr[i]=maxi
        if temp>maxi:
            maxi=temp
        
arr=[5,4,3,2,1]
greatest(arr)
