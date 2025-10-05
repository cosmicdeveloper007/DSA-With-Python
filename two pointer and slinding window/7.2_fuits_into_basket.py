def fruits_into_basket(arr):
    seen = {}         # Regular dictionary
    left = 0
    max_len = 0

    for right in range(len(arr)):
        fruit = arr[right]

        # Add fruit to basket
        if fruit in seen:
            seen[fruit] += 1
        else:
            seen[fruit] = 1

        # If more than 2 types, shrink window
        while len(seen) > 2:
            left_fruit = arr[left]
            seen[left_fruit] -= 1
            if seen[left_fruit] == 0:
                del seen[left_fruit]
            left += 1

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage
A = [1, 2, 1, 2, 3, 2, 2, 1]
print(fruits_into_basket(A))  # Output: 5