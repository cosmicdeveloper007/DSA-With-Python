# Longest Subarray with atmost k Zeroes

def Max_consecutive(arr , k):
    n = len(arr)
    result = []
    Max_len = 0

    for start in range(n):
        for end in range(start, n):
            subarray = arr[start:end + 1]
            result.append(subarray)

            if (subarray.count(0) <= k):
                Max_len = max(Max_len , len(subarray))
                print(subarray)

    return Max_len


if __name__ == "__main__":
    A = [1 , 1 , 1 ,0 , 0 ,1 ,0 , 1 ,1 , 0 , 0 , 1 , 1 , 0 , 0]
    k = 4

    print(Max_consecutive(A , k))