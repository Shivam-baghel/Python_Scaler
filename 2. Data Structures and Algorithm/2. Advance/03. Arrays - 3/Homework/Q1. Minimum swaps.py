""" 
Q1. Minimum Swaps

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.


Problem Constraints

1 <= length of the array <= 100000
-109 <= A[i], B <= 109


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return the minimum number of swaps.



Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:

 A = [5, 17, 100, 11]
 B = 20


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:

 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.

"""


def minSwaps(A, B):
    n = len(A)
    cnt = 0
    # count number of elements <= B
    for x in A:
        if x <= B:
            cnt += 1
    if cnt <= 1:
        return 0
    else:
        l, r, x = 0, 0, 0
        while r < cnt:
            if A[r] > B:
                x += 1
            r += 1
        ans = x
        # find the number of swaps required for each window of size cnt
        while r < n:
            if A[r] > B:
                x += 1
            if A[l] > B:
                x -= 1
            ans = min(ans, x)
            r += 1
            l += 1
    return ans
