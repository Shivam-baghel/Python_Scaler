"""
Given an aray of size N, find sum of all subarray's sums.

This question was asked in google type companies.
"""
# good method.
# time complexity O(n^2)
def sumOfSubarraySum(arr):
    ans = 0 
    for i in range(len(arr)):
        sumOfElement = 0
        for j in range(i,len(arr)):
            sumOfElement += arr[j]
        
        ans += sumOfElement
    
    print(ans)

# optamized method
# time complexity O(n)
def sumOfSubarraySum2(arr):
    totalSum = 0
    length = len(arr)
    for i in range(len(arr)):
        countOfelement = (i + 1)*(length - i)  # count of elements in subarrays.
        totalSum = totalSum + (arr[i]*countOfelement)

    print(totalSum)

arr = tuple(map(int,input().split()))
sumOfSubarraySum(arr)