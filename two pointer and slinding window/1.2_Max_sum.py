def max_sum(arr , k):
    n = len(arr)
    Window_sum = sum(arr[0:k])
    MaxSum = 0


    for i in range (k , n):
        
        Window_sum += arr[i] - arr[i-k]

        MaxSum = max(Window_sum, MaxSum) 

    return MaxSum

if __name__ == "__main__":
    A = [4 , 7 , 8 , 3 , 0 , 5 , 8 , 10 , 65 , 4]
    k = 3

    B = max_sum(A , k)
    print(B)