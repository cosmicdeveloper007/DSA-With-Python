# binary subarray with sum

def binary_subarray(arr , goal):

    if goal < 0 :
        return 0
    
    n = len(arr)
    left = 0 
    right = 0 
    count = 0 
    sum = 0

    while right < n :

        sum += arr[right]

        while sum > goal:
            sum -= arr[left]

            left += 1
        
        count += right - left + 1
        right += 1

    return count 

if __name__ == "__main__":
    A = [ 1 , 0 , 0 , 1 , 0 , 1  , 1 ,0 , 0 , 1 , 0 , 1 , 0 ]
    k = 2
    print(binary_subarray(A , k) - binary_subarray(A , k-1))

    # The total number of subarray having binary sum = k are Function(arr , goal) - Function(arr , goal-1)