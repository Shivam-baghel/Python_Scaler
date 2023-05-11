""" 
Q6. Linked-List
Design and implement a Linked List data structure.
A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:

insert_node(position, value) - To insert the input value at the given position in the linked list.
delete_node(position) - Delete the value at the given position from the linked list.
print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).
Note:

If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in a new line.

Problem Constraints
1 <= value <= 105
1 <= position <= n where, n is the size of the linked-list.

Input Format
First line contains an integer denoting number of cases, let's say t.
Next t line denotes the cases.

Output Format
When there is a case of print_ll(),  Print the entire linked list, such that each element is followed by a single space. There should not be any trailing space.
NOTE: You don't need to return anything.


Example Input
5
i 1 23
i 2 24
p
d 1
p

Example Output
23 24
24

Example Explanation
After first two cases linked list contains two elements 23 and 24.
At third case print: 23 24.
At fourth case delete value at first position, only one element left 24.
At fifth case print: 24.

"""
class Node:
    def __init__(self,data,next= None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None
        
ll = Linkedlist()
        
def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    
    # Insert a node at a given position in the LinkedList
    if position == 1:
        NewNode = Node(value)
        NewNode.next = ll.head
        ll.head = NewNode
    else:
        NewNode = Node(value)
        
    

def delete_node(position):
    # @param position, integer
    # @return an integer
    return

def print_ll():
    # Output each element followed by a space
