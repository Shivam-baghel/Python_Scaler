""" 
Q4. 3 Sum Zero

Jerry is excited about an array that Tom gave him. The array A consists of N integers.

Tom challenges Jerry to find all such unique triplets a, b, c in A such that a + b = - c.

Note:
Elements in a triplet (a,b,c) must be in non-decreasing order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.


Problem Constraints

0 <= N <= 7000
-108 <= A[i] <= 108


Input Format

Single argument representing a 1-D array A.



Output Format

Output a 2-D vector where each row represent a unique triplet.



Example Input

Input 1:
A = [-5, 2, 1, 3]
Input 2:
A = [-1, 0, 1, 2, -1, 4]


Example Output

Output 1:
[[-5, 2, 3]]
Output 2:
[[-1,0,1],
 [-1,-1,2] ]


Example Explanation

Explanation 1:
Out of all the possible triplets, the triplet (-5, 2, 3) only satisfies the condition, which is in the form [ (-5) + (2) = - (3) ]
Explanation 2:
Out of all the possible triplets only the above two triplets satisfies the condition and unique.

"""
