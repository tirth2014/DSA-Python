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



# Time Complexity  :  O(N)
# Space Complexity :  O(1)

from typing import Optional, Any


# Definition for node of singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, val: Any) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    def print_linked_list(self, head=None):
        temp = head if head else self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


class Solution:
    def ll_len(self, head):
        temp = head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        return len

    def reverse_k(self,head,k):
        temp = None
        curr = head
        cnt = 0
        while curr or cnt == k:
            if cnt == k:
                # 0.curr -> Next part head to check (tmp_head)
                # 1.head -> Original group head (curr_orig)
                # 2.temp -> Reversed group head (curr_rev)
                return curr,head,temp
            nxt = curr.next
            curr.next = temp
            temp = curr
            curr = nxt
            cnt  += 2 if curr == head else 1

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        possible_parts = (self.ll_len(head)) // k
        tmp_head = head
        prev_orig = False
        start = False
        while possible_parts:
            tmp_head, curr_orig, curr_rev = self.reverse_k(tmp_head,k)
            if not start:
                start = curr_rev
            possible_parts -= 1
            if prev_orig:
                prev_orig.next = curr_rev
            prev_orig = curr_orig
        prev_orig.next = tmp_head
        return start


if __name__ == '__main__':
    ll = LinkedList()
    input_string = input("Enter a list of elements separated by spaces or commas: ")
    ip_lst = list(map(int, input_string.replace(',', ' ').split()))
    for ele in ip_lst:
        ll.insert_at_end(ele)
    ll.print_linked_list()
    ob = Solution()
    k = int(input('k: '))
    newhead = ob.reverseKGroup(ll.head, k)
    ll.print_linked_list(newhead)

