""" Find the size of the linked List. """
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def sizeOfLinkedList(a):
    count = 0
    temp = a
    while temp:
        temp = temp.next
        count += 1
    
    return count