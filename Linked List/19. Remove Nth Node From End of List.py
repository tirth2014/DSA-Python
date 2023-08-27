# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach-1 ( 3 pass ):
# Time Complexity: O(N)
# Space Complexity: O(1)

# 1. Reverse the ll -                                                             O(N)
# 2. Remove the nth node -                                                        O(N) worst case
# 3. Again reverse the ll to get original ll with nth node from right deleted     O(N)

class Solution:
    def reverse_ll(self,head):
        temp = None
        nxt = head.next
        while head and head.next:
            head.next = temp
            temp = head
            head = nxt
            nxt = nxt.next
        head.next = temp
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        reversed_head = self.reverse_ll(head)
        prev = None
        curr = reversed_head
        if n == 1:
            reversed_head = reversed_head.next
            return self.reverse_ll(reversed_head)
        cnt = 1
        while cnt != n:
            cnt += 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return self.reverse_ll(reversed_head)



      
# Follow up: Could you do this in one pass?
