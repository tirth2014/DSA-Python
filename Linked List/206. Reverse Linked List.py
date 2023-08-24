# Iterative:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = None
        nxt = head.next
        while nxt:
            head.next = temp
            temp = head
            head = nxt
            nxt = nxt.next
        head.next = temp
        return head

# Recursive-1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # This will return last node which will ultimately be new_head

        new_head = self.reverseList(head.next)
        # From last second node to first node reverse pointers
        # But new_head will remain same in returning of all recursive calls..which will be last node
        head_next = head.next
        head_next.next = head
        head.next = None
        return new_head

# Recursive-2
class Solution:
    def _reverse_recursive(self,node=None,prev=None):
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return self._reverse_recursive(node=nxt,prev=node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse_recursive(head)
