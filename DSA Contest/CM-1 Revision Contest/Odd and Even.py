""" 
Odd Even Linked List

You are given the head A of a singly linked list of length N. You need to group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered linked list.

The first node is considered odd, and the second node is even, and so on.

The relative order inside both the even and odd groups should remain as it was in the initial linked list.

Note: You must solve the problem in O(1) extra space complexity and O(N) time complexity.



Problem Constraints
1 <= N <= 105

1 <= value of a node <= 109



Input Format
The only argument A is the head of the linked list



Output Format
Return a linked list.



Example Input
Input 1:

A = 1 -> 2 -> 3 -> 4 -> NULL 
Input 2:

A = 5 -> 7 -> 6 -> 2 -> 9 -> NULL


Example Output
Output 1:

1 -> 3 -> 2 -> 4 -> NULL
Output 2:

5 -> 6 -> 9 -> 7 -> 2 -> NULL


Example Explanation
Explanation 1:

The odd nodes of the linked list are 1 and 3 while the even nodes are 2 and 4.
Explanation 2:

The odd nodes of the linked list are 5, 6 and 9 while the even nodes are 7 and 2.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if A is None:
            return None
        odd = A
        even = A.next
        evenHead = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return A