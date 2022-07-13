"""
prefix array
what is prefix array
if we had array in cummulitive sum form it is called cummulitive sum array.
if the cummulitive sum from left to right it is called prefix sum array.
if the cummulitive sum is from right to left it is called suffix sum array
How to construct prefix array.

"""

arr = tuple(map(int,input().split()))
prefixArray = [0] * len(arr)
prefixArray[0] = arr[0]

for i in range(1,len(arr)):
    prefixArray[i] = prefixArray[i-1] + arr[i]

print(arr)
print(prefixArray)