# https://leetcode.com/problems/delete-node-in-a-linked-list/

"""
 # goal : delete node 2.

    1  ->  2 -> 3       -> 4  ->  5
           ^    ^
           |    |
          node  node.next
     #step one:  change the node value to 3
     1  ->  3   3           4  ->  5
           ^    ^           ^
           |    |           |
          node  node.next   node.next.next
          
      #step two: change the next pointer to point to node.next.next
     1  ->  3   ->          4   ->  5
           ^    ^           ^
           |    |           |
          node  node.next   node.next.next
    
  1 ->3 ->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Just this...nothing else complex needed to do. No need to traverse and change all values.
        node.val = node.next.val
        node.next = node.next.next



# My solution (Wrong...adds extra data at last)

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print(node)
        print()
        while node and node.next:
            orig_node = node
            node_next = node.next
            node.val = node_next.val
            node = node_next
            node_next.next = node_next.next
# Input                                  
# [4,5,1,9]
# 5
# Output
# [4,1,9,9]
# Expected
# [4,1,9]

# Input
# [500,10,4,5,1,9,-10,-11,100,8]
# 500
# Output
# [10,4,5,1,9,-10,-11,100,8,8]
# Expected
# [10,4,5,1,9,-10,-11,100,8]
