# minimum window string 

def minimum_window_string(s, t):
    m, n = len(t), len(s)
    if m > n: 
        return ""

    # Frequency map of t
    freq = {}
    for ch in t:
        freq[ch] = freq.get(ch, 0) + 1

    count = len(freq)   # how many unique chars still needed
    left = 0
    min_len = float("inf")
    start = 0   # to store answer substring start index

    for right in range(n):
        if s[right] in freq:
            freq[s[right]] -= 1
            if freq[s[right]] == 0:
                count -= 1

        # When all chars covered
        while count == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            # try shrinking
            if s[left] in freq:
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count += 1
            left += 1

    return "" if min_len == float("inf") else s[start:start+min_len]


if __name__ == "__main__":
    s = "xyzaacbbycazbca"
    t = "abc"
    print(minimum_window_string(s, t))  # 👉 "bca"
