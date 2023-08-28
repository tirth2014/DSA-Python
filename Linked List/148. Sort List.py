# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution - 1 (Naive)
# Gives TLE for big input
# Time Complexity: O(N * N*log(N))
class Solution:
    def ll_length(self,head):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        return int(length)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = None
        ll_len = self.ll_length(head)
      
        for _ in range(ll_len * int(math.log(ll_len, 2))):
            prev = None
            p1, p2 = head, head.next
            if head.val > head.next.val:
                new_head = head.next
            while p2:
                if p1.val > p2.val:
                    if prev:
                        prev.next = p2
                    p1.next = p2.next
                    p2.next = p1
                    prev = p2
                    p2 = p1.next
                else:
                    prev = p1
                    p1 = p1.next
                    p2 = p2.next
            head = new_head or head
        return head
