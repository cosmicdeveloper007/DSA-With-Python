# Longest repeating character replacement 

def Longest_susbtring(s , k):
    s.lowercase()
    n = len()
    max_len = 0
    left = 0
    count = 0

    for right in range(n):
        if s[right] != "a":
            count += 1
        
        while  count > k:
            if s[left] !=  "a":
                count -= 1
            left += 1

        max_len = max(max_len , right - left + 1)

    return max_len





    