# longest substring with atmost K distinct characters

def Longest_substring_with_k_distinct_characters(S , k):
    n = len(S)
    max_len = 0
    seen = {}
    left = 0  

    for right in range(n):

        if S[right] in seen:
            seen[S[right]] += 1
        else:
            seen[S[right]] = 1

        while len(seen) > k:
            seen[S[left]] -= 1
            
            if seen[S[left]] == 0:
                del seen[S[left]]
            
            left += 1
        
        max_len = max(max_len , right - left + 1)
    
    return max_len

if __name__ == "__main__":
    S = "vivekkanaiyalalsen"
    k = 2
    print(Longest_substring_with_k_distinct_characters(S , k))