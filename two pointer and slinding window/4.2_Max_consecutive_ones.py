# Longest Subarray with atmost k Zeroes

def Max_consecutive(arr, k):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            zero_count += 1

        while zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
        
        max_len = max(max_len , right - left + 1)

    return max_len

if __name__ == "__main__":
    A = [1 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1  , 0 , 1]
    k = 3
    print(Max_consecutive(A , k))