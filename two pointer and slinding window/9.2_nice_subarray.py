# binary subarray with sum

def nice_subarray(arr , goal):

    if goal < 0 :
        return 0
    
    n = len(arr)
    left = 0 
    right = 0 
    count = 0 
    sum = 0

    while right < n :

        sum += arr[right]%2

        while sum > goal:
            sum -= arr[left]%2

            left += 1
        
        count += right - left + 1
        right += 1

    return count 

if __name__ == "__main__":
    A = [1 ,1 ,2 ,1 ,1]
    k = 3

    print(nice_subarray(A , k ) - nice_subarray(A , k-1))