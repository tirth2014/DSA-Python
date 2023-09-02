# https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity  :  O(N)
# Space Complexity :  O(N)

class Solution:
    # O(N)
    def ll_len(self, head):
        temp = head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        return len
      
    # O(N)
    def reverse_k(self,head,k):
        temp = None
        curr = head
        cnt = 0
        while curr or cnt == k:
            if cnt == k:
                # 0.curr -> Next group's head to check
                # 1.head -> Original group head
                # 2.temp -> Reversed group head
                return [curr,head,temp]   
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt
            cnt  += 2 if curr == head else 1

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        possible_parts = (self.ll_len(head)) // k
        part_res = []
        tmp_head = head
        while possible_parts:
            res = self.reverse_k(tmp_head,k)
            tmp_head = res[0]
            possible_parts -= 1
            part_res.append(res)
          
        # O(N)
        for ind in range(len(part_res)):
            if ind == len(part_res)-1:
                part_res[ind][1].next = tmp_head
                break
            part_res[ind][1].next = part_res[ind+1][2]
        return part_res[0][2]
