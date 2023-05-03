""" 
Q2. Search in Bitonic Array!

Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
NOTE:
A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.

Problem Constraints
3 <= N <= 105
1 <= A[i], B <= 108
Given array always contain a bitonic point.
Array A always contain distinct elements.

Input Format

First argument is an integer array A denoting the bitonic sequence.
Second argument is an integer B.

Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.


Example Input
Input 1:
 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:
 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30

Example Output
Output 1:
 3
Output 2:
 -1

Example Explanation
Explanation 1:
 B = 20 present in A at index 3
Explanation 2:
 B = 30 is not present in A
"""

""" 
my idea is to first find bitonic point or index as this index will hold greatest value. example like a mountain.
search on the left side of the bitonic point and then right side. if any point to time you find value equal to B.
return.
"""
def bitonic(arr,low,high):
    length = len(arr)
    
    while low<=high:
        mid = (low+high)//2
        if mid > 0 and mid < length-1 and arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        if arr[mid-1] < arr[mid] and arr[mid]< arr[mid+1]:
            # go to right
            low = mid+1
        elif arr[mid-1] > arr[mid] and arr[mid] > arr[mid+1]:
            # go to left
            high = mid-1

def SearchInBitonic(arr,B):
    n = len(arr)
    #find the bitonic index
    bitIndex = bitonic(arr,0,n-1)
    
    # search in the left side of the bitonic index till bitonic index
    l = 0
    h = bitIndex
    while l <= h:
        m = (l+h)//2
        if arr[m] == B:
            return m
        elif arr[m] < B:
            l = m+1
        else:
            h = m-1
    
    # search in the right side of the bitonic index after the bitonic index.
    l = bitIndex+1
    h = n-1
    while l<=h:
        m = (l+h)//2
        if arr[m] == B:
            return m
        elif arr[m] > B:
            # go to right
            l = m+1
        else:
            h = m-1
    
    return -1

A = [3, 9, 10, 20, 17, 5, 1]
print(bitonic(A,0,len(A)-1))