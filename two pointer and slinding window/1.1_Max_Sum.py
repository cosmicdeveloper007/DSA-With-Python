def Max_SumArray(arr):
    n = len(arr)
    SubArray = []
    ms = 0

    for start in range(0 , n):
        cs = 0 
        for end in range(start , n):
            cs += arr[end]
            ms = max(cs , ms)

    return ms
               

A = [ 6 , 8 , 9 , 0 ,6 , 8, 3 , 7 ,4 , 8]
Max_SumArray(A)
print(Max_SumArray(A))