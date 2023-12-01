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


if __name__ == '__main__':
    a = [1, 2, 3, 5, 6, 8]
    k = 1
    print(max_subarray(a, k))
