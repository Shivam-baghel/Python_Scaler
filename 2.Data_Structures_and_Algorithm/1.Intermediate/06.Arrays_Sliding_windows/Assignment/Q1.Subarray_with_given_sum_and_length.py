""" 
Q1. Subarray with given sum and length

Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 104
1 <= B <= N
1 <= C <= 109

Input Format
First argument A is an array of integers.
The remaining arguments B and C are integers

Output Format
Return 1 if such a subarray exist and 0 otherwise

Example Input
Input 1:
A = [4, 3, 2, 6, 1]
B = 3
C = 11
Input 2:

A = [4, 2, 2, 5, 1]
B = 4
C = 6

Example Output
Output 1:
1
Output 2:

0

Example Explanation
Explanation 1:
The subarray [3, 2, 6] is of length 3 and sum 11.
Explanation 2:
There are no such subarray.
"""


def subarray_with_sum_and_length(A, B, C):
    arr = A
    length = B
    sum_till = C

    sum_of_len = 0
    len_of_arr = len(arr)
    for i in range(length):
        sum_of_len += arr[i]

    result = [sum_of_len]

    start = 1
    end = length
    while end < len_of_arr:
        sum_of_len += arr[end] - arr[start - 1]

        result.append(sum_of_len)
        start += 1
        end += 1

    for j in result:
        if j == sum_till:
            return 1

    return 0


if __name__ == '__main__':
    A = [4, 3, 2, 6, 1]
    B = 3
    C = 11
    print(subarray_with_sum_and_length(A, B, C))
