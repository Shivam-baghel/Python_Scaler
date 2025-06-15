""" 
Q2. Kth Smallest Element

Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.



Problem Constraints

1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 109



Input Format

The first argument is an integer array A.

The second argument is integer B.



Output Format

Return the Bth smallest element in given array.



Example Input

Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output

Output 1:

 2
Output 2:

 2


Example Explanation

Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.

"""


def kthsmallest(A, B):
    a = []
    for x in A:
        a.append(x)
    for i in range(0, B):
        # finding the minimum element from the remaining array
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[B - 1]
