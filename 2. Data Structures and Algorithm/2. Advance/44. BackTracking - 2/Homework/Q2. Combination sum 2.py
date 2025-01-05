""" 
Q2. Combination Sum II

Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.

Each number in A may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Warning:

DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.

Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.



Problem Constraints

1 <= N <= 20

Input Format

First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number.



Output Format

Return all unique combinations in A where the candidate numbers sums to B.



Example Input

Input 1:

 A = [10, 1, 2, 7, 6, 1, 5]
 B = 8
Input 2:

 A = [2, 1, 3]
 B = 3


Example Output

Output 1:

 [ 
  [1, 1, 6 ],
  [1, 2, 5 ],
  [1, 7 ], 
  [2, 6 ] 
 ]
Output 2:

 [
  [1, 2 ],
  [3 ]
 ]


Example Explanation

Explanation 1:

 1 + 1 + 6 = 8
 1 + 2 + 5 = 8
 1 + 7 = 8
 2 + 6 = 8
 All the above combinations sum to 8 and are arranged in ascending order.
Explanation 2:

 1 + 2 = 3
 3 = 3
 All the above combinations sum to 3 and are arranged in ascending order.
 
"""


def find_answer(A, B, index, total, current, result):
    if total == B:
        if current not in result:
            result.append(current.copy())
        return

    if index == len(A):
        return

    # take in sum
    total = total + A[index]
    current.append(A[index])
    find_answer(A, B, index + 1, total, current, result)
    total = total - A[index]
    del current[-1]

    # no take take in sum
    find_answer(A, B, index + 1, total, current, result)


def combinationSum(self, A, B):
    A.sort()
    result = []
    current = []
    total = 0
    index = 0
    find_answer(A, B, index, total, current, result)
    return result


# def combinationSum(self, A, B):

#     def countsubsum(arr,n,i,summ):
#         if i == n:
#             if summ == k:
#                 return 1
#             else:
#                 return 0
