# https://leetcode.com/problems/add-two-numbers/description/

# Time Complexity: O(max(len(l1),len(l2)))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        carry = 0
        new_head = ListNode(None)
        temp = new_head
        while l1 or l2:
            new_sum = carry + (l1 and l1.val or 0) + (l2 and l2.val or 0)
            l1, l2 = l1 and l1.next or None, l2 and l2.next or None
            carry = new_sum // 10
            node = ListNode(new_sum % 10)
            temp.next = node
            temp = node
        if carry:
            node = ListNode(carry)
            temp.next = node
        return new_head.next
      

# Same solution using divmod function of python to get div and mod

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        carry = 0
        new_head = ListNode(None)
        temp = new_head
        while l1 or l2 or carry:
            new_sum = carry + (l1 and l1.val or 0) + (l2 and l2.val or 0)
            l1, l2 = l1 and l1.next or None, l2 and l2.next or None
            carry,val = divmod(new_sum, 10)
            node = ListNode(val)
            temp.next = node
            temp = node
        return new_head.next
