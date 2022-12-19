""" 
Q5. Maximum array sum after B negations
Given an array of integers A and an integer B. You must modify the array exactly B number of times. In a single modification, we can replace any one array element A[i] by -A[i].

You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.

Problem Constraints
1 <= length of the array <= 5*105
1 <= B <= 5 * 106
-100 <= A[i] <= 100

Input Format
The first argument given is an integer array A.
The second argument given is an integer B.

Output Format
Return an integer denoting the maximum array sum after B modifications.

Example Input
Input 1:
 A = [24, -68, -29, -9, 84]
 B = 4
Input 2:
 A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
 B = 10

Example Output
Output 1:
 196
Output 2
 362

Example Explanation
Explanation 1:
 Final array after B modifications = [24, 68, 29, -9, 84]
Explanation 2:
 Final array after B modifications = [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]

"""
import heapq as heap

def MaxSum(array:list,mod:int):
    arrayList = []
    lengthOfArray = len(array)
    
    # insert the array values in a heap.
    for i in range(lengthOfArray):
        heap.heappush(arrayList,array[i])
    
    # Loop mod times
    for j in range(mod,0,-1):
        
        # Choose the minimumm negative number at any moment and modify it according to the question.
            #- if all numbers left are positive and operations left are even. then nothing needs to be changed just break the loop.
            #- If all the numbers left are positive and operations left are odd choose the min elemnt x and make it -x in the heap and break the loop.
        
        # as arrayList is heap first element of the heap is min element always.
        if arrayList[0] < 0:
            heap.heapreplace(arrayList,-(arrayList[0]))
        else:
            if j%2==0:
                break
            else:
                heap.heapreplace(arrayList,-(arrayList[0]))
                break
    
    # Add the values present it heap.
    ans = 0
    for k in arrayList:
        ans += k
    
    return ans

A = [24, -68, -29, -9, 84]
B = 4
print(MaxSum(A,B))