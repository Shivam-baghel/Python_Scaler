"""
Given an array of size N, print all subarray of a given array.
"""
from print_All_Values_Of_a_Subarray import printSubArray

def printAllSubarrays(arr, startIndex, endIndex):
    for i in range(startIndex, endIndex+1):
        for j in range(i,endIndex):
            printSubArray(arr,i,j)

arr = tuple(map(int,input().split()))
s = int(input())
e = int(input())
printAllSubarrays(arr,s,e)
