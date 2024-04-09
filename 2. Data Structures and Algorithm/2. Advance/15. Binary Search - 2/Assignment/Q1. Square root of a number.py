""" 
Q1. Square Root of Integer

Given an integer A. Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

NOTE: 
   The value of A*A can cross the range of Integer.
   Do not use the sqrt function from the standard library. 
   Users are expected to solve this in O(log(A)) time.


Problem Constraints
0 <= A <= 109


Input Format
The first and only argument given is the integer A.


Output Format
Return floor(sqrt(A))


Example Input
Input 1:

 11
Input 2:

 9


Example Output
Output 1:

 3
Output 2:

 3


Example Explanation
Explanation 1:
When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
Explanatino 2:
When A = 9 which is a perfect square of 3, so we return 3.
"""


def sqrt(A):
    # a = A
    # if a == 0:
    #     return 0

    # start = 1
    # end = a

    # while start <= end:
    #     mid = (start + (end-start))//2

    #     if mid <= a//mid:
    #         ans = mid
    #         start = mid + 1
    #     else:
    #         end = mid-1

    # return ans

    if A == 1:
        return 1
    # ret = int(A ** 0.5)
    # return ret
    low = 0
    high = A / 2 + 1
    while low + 1 < high:
        mid = low + (high - low) / 2
        square = mid**2
        if square == A:
            return mid
        elif square < A:
            low = mid
        else:
            high = mid
    return int(low)
