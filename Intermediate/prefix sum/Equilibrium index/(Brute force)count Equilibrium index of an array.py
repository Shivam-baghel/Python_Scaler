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

arr = tuple(map(int,input().split()))
count = 0

for i in range(len(arr)):
    leftsum =0
    rightsum = 0

    if i == 0:
        leftsum = 0
    else:
        for j in range(i):
            leftsum = leftsum + arr[j]
    
    if i == len(arr)-1 :
        rightsum = 0
    else:
        for k in range(i+1,len(arr)):
            rightsum = rightsum + arr[k]

    if leftsum == rightsum:
        count +=1
    
print(count)
