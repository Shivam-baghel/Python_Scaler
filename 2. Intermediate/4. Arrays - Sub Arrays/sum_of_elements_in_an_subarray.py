"""
Given an array of size N, find the sum of all elements in a given sub array.
"""
def addSubArray(arr, startIndex, endIndex):
    sumOfElements = 0
    for i in range(startIndex,endIndex+1):
        sumOfElements = sumOfElements + arr[i]

    return sumOfElements