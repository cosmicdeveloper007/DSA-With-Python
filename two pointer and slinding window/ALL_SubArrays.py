def all_subarrays(arr):
    n = len(arr)
    result = [] 

    for start in range(n):
        for end in range(start, n):
            subarray = arr[start:end + 1]
            result.append(subarray)

    return result

# Example usage
arr = [1, 2, 3]
subarrays = all_subarrays(arr)

for sub in subarrays:
    print(sub)