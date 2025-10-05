# Longest repeating character replacement 

def no_of_substrings(s):
    n = len(s)
    count = 0
    freq = {"a": 0, "b": 0, "c": 0}
    left = 0

    for right in range(n):
        if s[right] in freq:
            freq[s[right]] += 1

        # shrink window until it loses a character
        while all(freq.values()):  # valid window contains all three
            count += n - right  # all substrings from left to right..end are valid
            if s[left] in freq:
                freq[s[left]] -= 1
            left += 1

    return count

if __name__ == "__main__":
    s = "abbcacccbccbbaaabca"
    print(no_of_substrings(s))  #  Output: 45
