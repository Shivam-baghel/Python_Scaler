"""
Given N array elements, count no. of element having atleast 1 element greater than itself ?

EX :
a = [-3,-2,1,4,3,8,5,8]
ans = 6 as atleast 6 element have 1 element greater than them.
as 8 is two times 

"""

from cmath import inf


def solve(a):
    maxVal = -float('inf')
    for i in range(len(a)):
        if maxVal < a[i] :
            maxVal = a[i]

    count = 0

    for i in range(len(a)):
        if a[i] != maxVal :
            count += 1

    return count

a =[-3,-2,1,4,3,8,5,8]
print(solve(a))