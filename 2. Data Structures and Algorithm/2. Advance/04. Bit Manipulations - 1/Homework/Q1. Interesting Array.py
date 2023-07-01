""" 
Q1. Interesting Array
You have an array A with N elements. We have two types of operation available on this array :
We can split an element B into two elements, C and D, such that B = C + D.
We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?

Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 106

Input Format
The first argument is an integer array A of size N.

Output Format
Return "Yes" if it is possible otherwise return "No".

Example Input
Input 1:
 A = [9, 17]
Input 2:
 A = [1]

Example Output
Output 1:
 Yes
Output 2:
 No

Example Explanation
Explanation 1:
 Following is one possible sequence of operations -  
 1) Merge i.e 9 XOR 17 = 24  
 2) Split 24 into two parts each of size 12  
 3) Merge i.e 12 XOR 12 = 0  
 As there is only 1 element i.e 0. So it is possible.
Explanation 2:
 There is no possible way to make it 0.
"""

def solve(self, A):
    ans=0
    for i in A:
        ans = ans ^ i
    if ans & 1 :
        return "No"
    else:
        return "Yes"
"""
We have 2 options:

1. Split  an element A to B&C such that A = B + C
2. Merge two elements E&F to D such that D = E ^ F

Let’s use these two options to get an answer:
Arr=[1,2,3,4]
1. Merge all elements - 1^2^3^4 = 4 (associative property)
2. Split 4 into 2 + 2
3. Merge 2^2 = 0

Note: n^n = 0 as per property

Arr=[1,2,3,4,5]
1. Merge all elements - 1^2^3^4^5 = 1
2. Can’t split 1
"""