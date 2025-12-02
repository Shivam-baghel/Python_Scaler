"""
Q3. Pick from both sides!

You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.


Problem Constraints

1 <= N <= 105
1 <= B <= N
-103 <= A[i] <= 103


Input Format

First argument is an integer array A.
Second argument is an integer B.


Output Format

Return an integer denoting the maximum possible sum of elements you removed.



Example Input

Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3
 
Input 2:
 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4

Example Output

Output 1:
 8
 
Output 2:
 9


Example Explanation

Explanation 1:
 Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
 
Explanation 2:
 Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9

"""

def pickFromBothSides( A, B):
    Sum=0
    n=len(A)
    for i in range (B):
        Sum+=A[i]
    maxSum=Sum

    for i in range (0,B):
        Sum=Sum-A[B-i-1]+A[n-1-i]
        maxSum=max(Sum,maxSum)

    return maxSum


""" 
Approach using Prefix and Suffix Sums:

Maintain two arrays prefix[i] and suffix[i] where prefix[i] denotes sum of elements from index [0,i] and suffix[i] denotes sum of elements from index [i,N-1].

Now iterate from left and one by one pick elements from left for example: if you pick ‘a’ elements from left and remaining ‘k-a’ elements from right.
So the sum in this case will be prefix[a-1] + suffix[n-(k-a)]

Maintain the maximum among all and return it.

Time Complexity: O(N)
Space Complexity: O(N)

where N is number of elements in array A

Bonus: Try solving it in O(1) space.

"""

import mainTest

def pickBothSides( A, B):
    
    n = len(A)
    
    # create a prfix sum array
    preArray = [0]*n
    preArray[0] = A[0]
    
    for i in range(1,n):
        preArray[i] = preArray[i-1] + A[i]
    
    # create a suffix sum array
    suffArray = [0]*n
    suffArray[n-1] = A[n-1]
    
    for i in range(n-2,-1,-1):
        suffArray[i] = suffArray[i+1] + A[i]
        
    ans = max(preArray[B-1],suffArray[n-B])
    
    for i in range(1,B):
        sum = preArray[i-1] + suffArray[n-(B-i)]
        ans = max(ans,sum)
    
    return ans
    
    
if __name__ == "__main__": 
    
    A = [5, -2, 3 , 1, 2]
    B = 3
    
    mainTest
    print(pickBothSides(A,B))
