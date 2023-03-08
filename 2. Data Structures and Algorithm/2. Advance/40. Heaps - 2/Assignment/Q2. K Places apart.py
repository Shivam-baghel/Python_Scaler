""" 
Q2. K Places Apart
N people having different priorities are standing in a queue.
The queue follows the property that each person is standing at most B places away from its position in the sorted queue.
Your task is to sort the queue in the increasing order of priorities.
NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity O(NlogB).

Problem Constraints
1 <= N <= 100000
0 <= B <= N

Input Format
The first argument is an integer array A representing the priorities and initial order of N persons.
The second argument is an integer B.

Output Format
Return an integer array representing the sorted queue.

Example Input
Input 1:
 A = [1, 40, 2, 3]
 B = 2
Input 2:
 A = [2, 1, 17, 10, 21, 95]
 B = 1

Example Output
Output 1:
 [1, 2, 3, 40]
Output 2:
 [1, 2, 10, 17, 21, 95]


Example Explanation
Explanation 1:
 Given array A = [1, 40, 2, 3]
 After sorting, A = [1, 2, 3, 40].
 We can see that difference between initial position of elements amd the final position <= 2.
Explanation 2:
 After sorting, the array becomes [1, 2, 10, 17, 21, 95].
"""
import heapq as heap

def KPlacesApart(A:list,B:int):
        #size of the array.
        lengthOfArray = len(A)
        # check if B = 0.
        if B == 0:
            return A

        # create a answer array
        ans = []

        # create a min heap array
        minHeap = []
        
        # Push elements from 0 --> B in min Heap
        for i in range(B):
            heap.heappush(minHeap,A[i])

        # iterate through B --> lengthOfArray.
            #- push the next element in minHeap
            #- pop min element from minHeap and put it in ans array.
            # - remember after going through the entire array. B elements will still remain in minHeap as you are iterating through b --> n.
        for i in range(B,lengthOfArray):
            heap.heappush(minHeap,A[i])
            ans.append(heap.heappop(minHeap))

        # Push all the min element one by one in ans array.
        while minHeap:
            ans.append(heap.heappop(minHeap))

        return ans
    
A = [ 25, 16, 11, 31, 28, 20, 3, 8 ]
B = 6
print(KPlacesApart(A,B))