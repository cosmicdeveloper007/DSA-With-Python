# Number of Substrings containing all three characters 

def No_of_substrings(s):
    n = len(s)
    result = []
    count = 0 

    for left in range(n):
        seen = {"a" : 0 , "b" : 0 , "c" : 0} 
        for right in range(left , n):
            if s[right] in seen:
                seen[s[right]] +=1

            if all(seen.values()):
                count += n-right
                break

    return count

if __name__ == "__main__":
    s = "abbcacccbccbbaaabca"
    print(No_of_substrings(s))