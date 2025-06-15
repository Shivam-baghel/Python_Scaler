"""
Q3. Jumping Along Towers.
you are given a one dimensional array A of size N. denoting the heights of N towers labelled from 1 to N. you are initailly standing at tower 1 your goal is to reach tower N. you can perform two types of jumps.
1. jump from (i)th tower to (i+1)th tower and this will cost you B*(A[i+1]-A[i]).
2. jump from (i)th tower to (i+2)th tower and this will cost you C*(A[i+2]-A[i]).
    find and return minimum cost incurred to reach tower N.
"""


def minCost(A, B, C):
    n = len(A)
    dp = [0] * n

    # Initializing the base cases
    dp[0] = 0
    dp[1] = B * abs(A[1] - A[0])

    # Filling the dp[] array in a bottom-up manner
    for i in range(2, n):
        dp[i] = min(
            dp[i - 1] + B * abs(A[i] - A[i - 1]), dp[i - 2] + C * abs(A[i] - A[i - 2])
        )

    return dp[n - 1]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
