"""
Given and array of size N, How many sub array can there be.
Example:
array of size N = [0,1,2,3,4,5,6]
Sub arrays : 
[0],[0,1].....[0,1,2,3,4,5,6] = n
[1],[1,2].....[1,2,3,4,5,6] = n-1
.....
[5],[5,6] = 2
[6] = 1

Total sub arrays = 1+2+3.....+n-1+n   This is an a.p n*(n+1)/2

"""
arr = tuple(map(int,input().split()))

# No of sub arrays

Number = len(arr)
count = (Number*(Number+1))//2  # double // is to convert the number in int.
print(count)