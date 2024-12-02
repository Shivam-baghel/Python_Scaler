""" 
Q2. All Unique Permutations

Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.

NOTE: No 2 entries in the permutation sequence should be the same.

WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. 
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.


Problem Constraints

1 <= |A| <= 9
0 <= A[i] <= 10


Input Format
Only argument is an integer array A of size N.

Output Format
Return a 2-D array denoting all possible unique permutation of the array.

Example Input

Input 1:
A = [1, 1, 2]

Input 2:
A = [1, 2]


Example Output

Output 1:
[ [1,1,2]
  [1,2,1]
  [2,1,1] ]
  
Output 2:
[ [1, 2]
  [2, 1] ]


Example Explanation

Explanation 1:
 All the possible unique permutation of array [1, 1, 2].
 
Explanation 2:
 All the possible unique permutation of array [1, 2].
 
"""
import sys

sys.setrecursionlimit(1000000000)

# checked the video solution and found need to use frequency array together backtracking concept.


def allUniquePermutation(arr: list, n: int):

    result = []
    hashArray = [0] * 11
    current = []

    for item in arr:
        hashArray[item] = hashArray[item] + 1

    generateUniquePermutation(arr, result, current, hashArray, n)

    return result


def generateUniquePermutation(
    arr: list, resultArr: list, currentArr: list, freqArray: list, length
):

    if len(currentArr) == length:
        resultArr.append([num for num in currentArr])

    for i in range(0, 11):

        if (freqArray[i]) > 0:

            freqArray[i] = freqArray[i] - 1
            currentArr.append(i)
            generateUniquePermutation(arr, resultArr, currentArr, freqArray, length)
            freqArray[i] = freqArray[i] + 1
            currentArr.pop()

    # result = []
    # hashArray = [0] * 10
    # current = []

    # for item in arr:
    #     hashArray[item] = hashArray[item] + 1

    # generateUniquePermutation(arr, result, current, hashArray, length)

    # return result


if __name__ == "__main__":
    # A = [1, 1, 2]
    A=[9,9,10,10,10]
    arrLength = len(A)
    print(allUniquePermutation(A, arrLength))
    # print(generateUniquePermutation(A, [], [], [], arrLength))
