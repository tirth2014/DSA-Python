"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using visited set to keep track of visited nodes ( Brute Force)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp = head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
      
# Solution-2: Marking nodes as visited by changing value to 'x'      
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp:
            if temp.val == 'x':
                return True
            temp.val = 'x'
            temp = temp.next
        return False

# Tortoise and hare algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
      
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
            if slow == fast:
                return True
        return False  
