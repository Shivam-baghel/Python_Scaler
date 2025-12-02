""" 
Q4. Pairs with given sum II

Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the number of pairs for which sum is equal to B modulo (10^9+7).



Example Input
Input 1:

A = [1, 1, 1]
B = 2
Input 2:

A = [1, 5, 7, 10]
B = 8


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

 The pairs of A[i] and A[j] which sum up to 2 are (0, 1), (0, 2) and (1, 2).
 There are 3 pairs.
Explanation 2:

 There is only one pair, such that i = 0, and j = 2 sums up to 8.
"""




""" 
SOLUTION APPROACH

Let us formulate a two pointer approach to the this problem.
We will first sort the given array and use two pointers i and j with i = 0, j = Length of Array - 1.
We will have three conditions:

1. A[i] + A[j] < sum  --> We will increase the pointer i.
2. A[i] + A[j] > sum  --> We will decrease the pointer j.
3. A[i] + A[j] = sum  --> We will count the frequency of A[i] and A[j] and multiply them and add to the answer.
Note, that if A[i] and A[j] are equal in value, then we will have to change the formula instead:
freq(A[i]) * freq(A[i]) –> freq(A[i]) * (freq(A[i]) - 1) / 2
to avoid overcounting pairs.

"""
def pairsWithGiveSum2( A, B):
    n = len(A)
    i, j = 0, n - 1
    mod = int(10 ** 9 + 7)
    ans = 0
    while (i < j):
        if (A[i] + A[j] == B):
            ii, jj = i, j
            if (A[i] == A[j]):
                # equal A[i] and A[j]
                cnt = j - i + 1
                ans += (cnt * (cnt - 1) // 2) % mod
                ans %= mod
                break
            else:
                # count number of elements with value A[i]
                while (A[i] == A[ii]):
                    ii += 1
                cnt1 = ii - i
                i = ii
                # count number of elements with value A[j]
                while (A[jj] == A[j]):
                    jj -= 1
                cnt2 = j - jj
                j = jj
                ans += (cnt1 * cnt2) % mod
                ans %= mod
        elif (A[i] + A[j] > B):
            j -= 1
        else:
            i += 1
    return ans