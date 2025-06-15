"""
Given an array of size N, print all the values of the array.

"""


def printSubArray(arr, startIndex, endIndex):
    for i in range(startIndex, endIndex + 1):  # goes through the values from start Index to lastIndex
        print(arr[i])  # print the particular value.


arr = tuple(map(int, input().split()))  # accepts a arra
printSubArray(arr, 0, len(arr))
