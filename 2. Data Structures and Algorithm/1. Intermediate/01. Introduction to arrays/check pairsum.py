"""
Given N array element , check if there exist a pair (i,j) such that 
arr[i] + arr[j] == k && i!=j
Note: i and j are index values.

Hint: whenever there is check present in the question this means that return type of the question is boolean.
"""

# Brute force method

from operator import truediv


def checkSum(arr, k):
    # here we are checking every single pair combination that is possible by i and j.
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] + arr[j] == k) and (i != j):
                return True

    return False


# optamised method

# here we know that we have to check every single possible pair combination of i and j.
# but many of those combination will be repeated as (i,j) and (j,i) are same pair.

def checkSum2(arr, k):
    for i in range(len(arr)):
        for j in range(i):  # here we are only going till i-1. so repeated same pair won't be comming across.
            if arr[i] + arr[j] == k:
                return True

    return False


a = tuple(map(int, input().split()))
k = int(input())
print("unoptimised method =", checkSum(a, k), "optimized method =", checkSum2(a, k))
