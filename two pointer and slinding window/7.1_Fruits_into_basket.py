# fruits into the basket but only 1 type of food can be stored in one basket 
# and there are total 2 baskets , maximum fruits stored in both are  ?

from collections import defaultdict

def fruits_into_basket(arr):
    seen = defaultdict(int)
    n = len(arr)
    Max_len = 0
    left = 0

    for right in range(n):
        
        seen[arr[right]] += 1

        while len(seen) > 2: 
            seen[arr[left]] -= 1
            if seen[arr[left]] == 0:
                del seen[arr[left]]
            left += 1

        Max_len = max(Max_len , right - left + 1)

    return Max_len

if __name__ == "__main__":
    A = [3 , 3 , 3 , 2 , 2 , 1 , 1 , 2 , 2 , 3 , 2 , 2 , 3 , 1]
    print(fruits_into_basket(A))