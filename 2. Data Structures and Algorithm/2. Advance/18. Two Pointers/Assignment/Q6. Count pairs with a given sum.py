""" 
Q6. Count of pairs with the given sum

Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.


Input Format

The first argument given is the integer array A.
The second argument given is integer B.
Output Format

Return the number of pairs for which sum is equal to B.
Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
1 <= B <= 10^9
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 5
Output 1:
    2

Input 2:
    A = [5, 10, 20, 100, 105]
    B = 110
Output 2:
    2
    
"""


def countPairsWithSum(A, B):
    p1 = 0
    p2 = len(A) - 1
    count = 0
    while p1 < p2:
        if A[p1] + A[p2] == B:
            count += 1
            # decrease the sum. that means moving pointer 2.
            p2 -= 1
        elif A[p1] + A[p2] > B:
            # decrease the sum.
            p2 -= 1
        else:
            # increase the sum.
            p1 += 1

    return count
