""" 
Q1. Delete middle node of a Linked List
Given a singly linked list, delete middle of the linked list.

For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

Return the head of the linked list after removing the middle node.

If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


Input Format

The only argument given is the node pointing to the head node of the linked list

"""

import hi

# Definition for singly-linked list.
# class Node:
#    def __init__(self, x):
#        self.data = x
#        self.next = None

def getMid(head):
    count = 0
    while head:
        count +=1
        head = head.next
    mid = count//2
    return mid

def deleteMid(head):
    
    No
    if not head:
        return head