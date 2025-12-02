""" 
Q3. Max Distance


Given an array, A of integers of size N. Find the maximum value of j - i such that A[i] <= A[j].


Problem Constraints

1 <= N <= 105
-109 <= A[i] <= 109


Input Format

First argument is an integer array A of size N.



Output Format

Return an integer denoting the maximum value of j - i.



Example Input

Input 1:

A = [3, 5, 4, 2]
Input 2:

A = [4, 1, 3, 0]


Example Output

Output 1:

2
Output 2:

1


Example Explanation

Explanation 1:

For A[0] = 3 and A[2] = 4, the ans is (2 - 0) = 2. 
Explanation 2:

For A[1] = 1 and A[2] = 3, the ans is (2 - 1) = 1. 

"""


def maximumGap(A):
    n = len(A)

    # Creation of Minimum_Prefix
    pf_min = [0 for i in range(n)]
    pf_min[0] = A[0]
    for i in range(1, n):
        if A[i] < pf_min[i - 1]:
            pf_min[i] = A[i]
        else:
            pf_min[i] = pf_min[i - 1]

    # Creation of Maximum_Suffix
    pf_max = [0 for i in range(n)]
    pf_max[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        if A[i] > pf_max[i + 1]:
            pf_max[i] = A[i]
        else:
            pf_max[i] = pf_max[i + 1]

    # intialzing ans to -1 since we use max function
    ans = -1
    i = 0
    j = 0

    # using while loop to keep track of Maximum_Prefix and Minimum_Prefix separately
    while j < n and i < n:
        if pf_min[i] <= pf_max[j]:
            ans = max(ans, (j - i))
            # We are incrementing index of Maximum_Prefix since the condition satisfies
            j += 1
        else:
            # We are incrementing the index of Minimum_Prefix_Prefix since the condition is not satisfied and we need to reduce the pf_min value to match the condition.
            i += 1
    return ans
