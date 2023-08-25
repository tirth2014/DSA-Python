"""
https://leetcode.com/problems/linked-list-cycle-ii/description/
https://takeuforward.org/data-structure/starting-point-of-loop-in-a-linked-list/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

#Ex:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Brute Force approach- maintaining set/list data structure to keep track of visited nodes:
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        temp = head
        while temp and temp not in visited:
            visited.add(temp)
            temp = temp.next
        return temp


# Optimal approach - Tortoise and Hare Algorithm

# Intuition:
# Length from head to start of cycle = L1
# Length from cycle start to slow and fast pointer collision point = L2
# Slow covers distance = L1 + L2
# fast = 2 x slow
# Fast covers distance = (L1 + L2) + nC
# n = no. of rounds/cycles
# C = length of cycle
# (L1 + L2) + nC = 2(L1 + L2)
# L1 + L2 = nC
# L1 = nC - L2

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        slow = fast = entry = head
      
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
        
