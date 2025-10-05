# Number of Subarrays with k different integer 

def Subarrays_with_k_dintinct_integer(arr , k):

    n = len(arr)
    left = 0 
    count = 0
    seen = {}

    for right in range (n) :

        if arr[right] in seen:
            seen[arr[right]] += 1
        else:
            seen[arr[right]] = 1

        while len(seen) > k:
            seen[arr[left]] -= 1

            if seen[arr[left]] == 0:
                del seen[arr[left]]
            
            left += 1
    
        count += right - left + 1
    
    return count 

if __name__ == "__main__":
    A = [1 , 1 , 2, 3, 1 , 4, 2, 8 ,  8 , 9 ,  1 , 2]
    k = 3
    print(Subarrays_with_k_dintinct_integer(A , k) - Subarrays_with_k_dintinct_integer(A , k-1))