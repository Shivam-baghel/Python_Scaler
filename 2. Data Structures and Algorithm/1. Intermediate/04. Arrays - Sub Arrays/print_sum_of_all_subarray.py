"""
Given an array of size N, print  the sum of every single subarray.
"""
from sum_of_elements_in_an_subarray import addSubArray

# Brute force method.

# def sumOfAllSubArray(arr):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             s = addSubArray(arr,i,j)
#             print(s, end= " ")

# optamized code

def sumOfAllSubArray(arr):
    for i in range(len(arr)):
        sumOfElements = 0
        for j in range(i,len(arr)):
            sumOfElements = sumOfElements + arr[j]
            print(sumOfElements)

arr = tuple(map(int,input().split()))

sumOfAllSubArray(arr)