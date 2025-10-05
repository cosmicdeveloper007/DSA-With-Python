# Maximum points you can obtain from cards by taking 
# elements from end or start only such that total elements = k

def Maximum_points (nums , k):
    n = len(nums)
    Lsum = 0
    Rsum = 0

    for i in range(0 , k):
        Lsum += nums[i]

    Max_sum = Lsum

    Rindex = n-1
    for i in range(k-1 , -1 , -1):
        Lsum -= nums[i]
        Rsum += nums[Rindex]
        Rindex -= 1

        Max_sum = max(Max_sum , Lsum + Rsum)

    return Max_sum

if __name__ == "__main__":
    Array = [ 6 ,2 , 3 , 4 , 7 , 2 , 1 , 7 , 1]
    k=4
    print(Maximum_points(Array , k))