# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Both approach have same time (O(N)) and space complexity (O(1)).
# Approach-1:

class Solution:
    def find_length(self,head):
        temp = head
        ll_len = 0
        while temp:
            ll_len += 1
            temp = temp.next
        return ll_len
      
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        else:
            ll_len = self.find_length(head)//2
            middle_ind = ll_len + 1

            temp = head
            while temp:
                middle_ind -= 1
                if middle_ind == 0:
                    head = temp
                    return head
                temp = temp.next

# Approach-2:
# Tortoise and hare (slow and fast)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        kachbo = saslu = head  # slow and fast both at first node initially
        while saslu and saslu.next:
            kachbo = kachbo.next
            saslu = saslu.next.next
        
        # when fast reaches the end, slow will be at middle of ll.
        return kachbo
