# https://www.codingninjas.com/studio/problems/reverse-a-doubly-linked-list_1116098

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''
# Recursive solution:
def reverseDLL(head):

    if not head or not head.next:
        return head

    new_head = reverseDLL(head.next)

    head_next_next = head.next.next
    head.next.next = head
    head.next.prev = head_next_next
    head.prev = head.next
    head.next = None
    return new_head


# Iterative solution:
def reverseDLL(head):
    prev_temp = None
    curr = head
    while curr:
        curr_next = curr.next  # Store the next node of curr in the original list to ensure that it's not lost during the reversal process.
        curr.next = prev_temp  # Update the 'next' pointer of the current node to point backwards
        curr.prev = curr_next  # Update the 'prev' pointer of the current node to point forwards
        prev_temp = curr       # Move the previous pointer to the current node
        curr = curr_next       # Move the current pointer to the next node in the original list
    return prev_temp # At the end return the last node which is now new head 
