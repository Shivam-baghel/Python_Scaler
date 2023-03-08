""" 
Q2. Closest MinMax 
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

Example Input
Input 1:
A = [1, 3]
Input 2:
A = [2]

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 Only choice is to take both elements.
Explanation 2:
 Take the whole array.
"""

def closestMinMax(ar):
    n = len(ar)
    # get min and max values from array.
    min_value = min(ar)
    max_value = max(ar)
    # if min and max value is same then directly return 1
    if min_value == max_value:
        return 1
    # minPointer and maxPointer will point towards the indexes of the min and max values.
    minPointer = -1 
    maxPointer = -1
    
    # size represents the length of the smallest subarray with min and max value present inside the subarray
    size = n
    # loopin on the array
    for i in range(n):
        # if values of i is equal to minimum value change minPointer to that particular index.
        if ar[i] == min_value:
            minPointer = i
        # if values of i is equal to maximum value change maxPointer to that particular index.
        elif ar[i] == max_value:
            maxPointer = i
        # check if max and min pointer are not equal to -1
        if minPointer != -1 and maxPointer != -1:
            size = min(size,abs(maxPointer-minPointer)+1)
            
    return size

ar = [ 814, 761, 697, 483, 981 ]
print(closestMinMax(ar))