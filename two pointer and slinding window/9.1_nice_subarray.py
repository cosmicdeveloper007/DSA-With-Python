# Count the number of Nice subarrays 

def nice_subarray(arr , k):

    n = len(arr)
    count = 0
    left = 0
    Max_count = 0

    for right in range(n):
        if arr[right]%2 == 1 :
            count += 1

        while count > k :
            if arr[left]%2 == 1 :
                count -= 1

            left += 1
        Max_count += right - left + 1
        

    return  Max_count

if __name__ == "__main__":
    A = [1 ,1 ,2 ,1 ,1]
    k = 3

    print(nice_subarray(A , k ) - nice_subarray(A , k-1))