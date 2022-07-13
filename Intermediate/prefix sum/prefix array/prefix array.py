"""
prefix array
what is prefix array
if we had array in cummulitive sum form it is called cummulitive sum array.
if the cummulitive sum from left to right it is called prefix sum array.
if the cummulitive sum is from right to left it is called suffix sum array
How to construct prefix array.

"""

arr = tuple(map(int,input().split()))       # accepting the array
prefixArray = [0] * len(arr)                # creating a new different array for prefix array
prefixArray[0] = arr[0]                     # make the first element of the prefix array equal to the first element of the array.               

for i in range(1,len(arr)):
    prefixArray[i] = prefixArray[i-1] + arr[i]      # populating the prefix array.

print(arr)
print(prefixArray)      # printing the prefix array