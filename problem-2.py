def seg(arr):

    p = ([x for x in arr if x==0] + [x for x in arr if x==1])

    print(p)

if __name__ == "__main__":

    a = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

    seg(a) 
