"""

Problem Description:

You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.
"""
def checkEquilibriumIndex(arr):

    prefixArray = [0]*len(arr)
    prefixArray[0] = arr[0]
    
    for i in range(1,len(arr)):
        prefixArray[i] = prefixArray[i-1] + arr[i]

    flag = 0
    length = len(arr)
    returnIndex = len(arr)
    for i in range(length):

        if i == 0:
            leftSum = 0
        else:
            leftSum = prefixArray[i-1]
        
        rightSum = prefixArray[length-1] - prefixArray[i]

        if leftSum == rightSum:
            flag +=1
            index = i

            returnIndex = min(returnIndex,index)
    
    if flag > 0:
        return returnIndex
    else:
        return -1

arr = tuple(map(int,input().split()))
print(checkEquilibriumIndex(arr))