"""
Q5. Max subarray with length k
Given an array A of length N. Find the Maximum sum of the subarray of length K.
"""


# optamised brute force approach
def max_subarray(arr: list, k: int):
    length_of_arr = len(arr)
    result = float('-inf')

    start = 0
    end = k

    while end <= length_of_arr:
        sum_of_subarr = 0
        for i in range(start, end):
            sum_of_subarr += arr[i]

        if sum_of_subarr > result:
            result = sum_of_subarr

        start += 1
        end += 1

    return result


# Optamised carry forword or sliding window approach
def max_subarray2(arr: list, k: int):
    n = len(arr)
    sum_of_arr = 0
    for i in range(0, k):
        sum_of_arr += arr[i]

    result = sum_of_arr
    start = 1
    end = k

    while end < n:
        sum_of_arr += arr[end] - arr[start - 1]

        if sum_of_arr > result:
            result = sum_of_arr

        start += 1
        end += 1

    return result


if __name__ == '__main__':
    a = [1, 2, 3, 5, 6, 8]
    k = 2
    print(max_subarray(a, k))
    print(max_subarray2(a,k))
