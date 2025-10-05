# Longest substring withour any repeating characters 

def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0
    n = len(s)

    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len , right - left  + 1)

    return max_len


if __name__ == "__main__":
    s = "pwwkew"
    print(length_of_longest_substring(s))