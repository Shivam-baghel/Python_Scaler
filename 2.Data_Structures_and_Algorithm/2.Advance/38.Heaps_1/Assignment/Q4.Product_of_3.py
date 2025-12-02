""" 
Q4. Product of 3
Given an integer array A of size N.
You have to find the product of the three largest integers in array A from range 1 to i, where i goes from 1 to N.
Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i in B should be -1.

Problem Constraints
1 <= N <= 105
0 <= A[i] <= 103

Input Format
First and only argument is an integer array A.

Output Format
Return an integer array B. B[i] denotes the product of the largest 3 integers in range 1 to i in array A.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [10, 2, 13, 4]

Example Output
Output 1:
 [-1, -1, 6, 24, 60]
Output 2:
 [-1, -1, 260, 520]

Example Explanation
Explanation 1:
 For i = 1, ans = -1
 For i = 2, ans = -1
 For i = 3, ans = 1 * 2 * 3 = 6
 For i = 4, ans = 2 * 3 * 4 = 24
 For i = 5, ans = 3 * 4 * 5 = 60
 
 So, the output is [-1, -1, 6, 24, 60].
 
Explanation 2:
 For i = 1, ans = -1
 For i = 2, ans = -1
 For i = 3, ans = 10 * 2 * 13 = 260
 For i = 4, ans = 10 * 13 * 4 = 520

 So, the output is [-1, -1, 260, 520].
"""
import heapq as heap
def productOfThree(array:list):
    ans = [-1,-1]
    l = []
    heap.heapify(l)
    # insert the first three values in heap and store the multiple of the three values too.
    mul = 1
    for i in range(3):
        heap.heappush(l,array[i])
        mul = mul*array[i]
    # append the multiple in ans list
    ans.append(mul)
    for j in range(3,len(array)):
        # if value is greater than the values present in the min heap push the value in min heap and pop min value from the min heap.
            #- multipley ther pushed value and divide the poped value in mul variable.
            #- append the mul to ans list
        # else just append the previous multiple to ans list
        if array[j] > l[0]:
            mul = mul*array[j]
            div = heap.heappushpop(l,array[j])
            # heap.heappush(l,array[j])
            # div = heap.heappop(l)
            mul = mul//div
            ans.append(mul)
        else:
            ans.append(mul)

    
    
    
    return ans

A = [1,2,3,4,5]
print(productOfThree(A))