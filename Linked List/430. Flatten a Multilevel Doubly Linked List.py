# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


# Recursion-1 (Not optimized)
class Solution:
    def flatten_recursively(self,head):
        temp = head
        prev = None
        while temp:
            if temp and temp.child:
                temp_nxt = temp.next
                child_last = self.flatten_recursively(temp.child)
                temp.next = temp.child
                temp.child.prev = temp
                child_last.next = temp_nxt
                if temp_nxt:
                    temp_nxt.prev = child_last
                temp.child = None
            prev = temp
            temp = temp.next
        return prev

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = self.flatten_recursively(head)
        return head




# Recursion-2 (Optimized - beats 100%)
class Solution:
    def flatten_recursively(self,temp):
        while not temp.child and temp.next:
            temp = temp.next
        if temp.child:
            child_last = self.flatten_recursively(temp.child)  # We'll get tail node of child with this recursive call.
        else:
            return temp     # Return node in case it's the last node in list of particular level
        temp_nxt = temp.next
        temp.next = temp.child
        temp.child.prev = temp
        temp.child = None

        if temp_nxt:
            child_last.next = temp_nxt
            temp_nxt.prev = child_last
            while temp_nxt.next:
                temp_nxt = temp_nxt.next
            return temp_nxt
        else:
            return child_last

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            self.flatten_recursively(head)
        return head


# Recursion - 3:
"""
This function modifies the structure in place. It's not the fastest implementation out there.

The trick to make this work is to add a second parameter to the function signature. 
A call to flatten(head, rest) will flatten the head and concatenate the rest to the end of it. That allows our recursive definition:

head.next = self.flatten(head.child, self.flatten(head.next,rest))

"""
class Solution:

    def flatten(self, head: 'Optional[Node]', rest = None) -> 'Optional[Node]':
        if not head: 
            return rest

        head.next = self.flatten(head.child, self.flatten(head.next,rest))
        
        if head.next:
            head.next.prev = head
        head.child = None
        
        return head
        


# dfs approach Using stack and order list
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        stack, order = [head], []

        while stack:
            last = stack.pop()
            order.append(last)
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)

        for i in range(len(order)-1):
            order[i+1].prev = order[i]
            order[i].next = order[i+1]
            order[i].child = None

        return order[0]



# dfs approach using stack without maintaining extra order list
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        dummy = Node(None)
        stack, curr = [head], dummy
        while stack:
            last = stack.pop()
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
            curr.next = last
            last.prev = curr
            last.child = None
            curr = last
        res = dummy.next
        res.prev = None
        return res

        
