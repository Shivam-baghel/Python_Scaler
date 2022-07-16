"""
Problem Description:

You are given an array A of integers of size N.
Your task is to count the no of equilibrium index's of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.

"""
def countNoOfEquilibriumIndex(prefixArray):

    for i in range(len(arr)):
        leftSum = 0
        rightSum = 0

        if i == 0:
            continue
        else:
            leftSum = prefixArray[i-1] - prefixArray[0]

