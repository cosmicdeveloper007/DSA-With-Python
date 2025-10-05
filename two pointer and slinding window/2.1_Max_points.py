# Maximum points you can obtain from cards by taking elements 
# from end or start only such that total elements = k


def maximum_points(arr , k):
    n = len(arr)
    Sum1 = sum(arr[-k:])
    Max_Sum = Sum1

    for i in range(-k, 0):
        Sum1 += arr[i+k]-arr[i]
        Max_Sum = max(Max_Sum , Sum1)
       
    return Max_Sum

if __name__ == "__main__":
    Array = [ 6 ,2 , 3 , 4 , 7 , 2 , 1 , 7 , 1]
    k=4
    print(maximum_points(Array , k))