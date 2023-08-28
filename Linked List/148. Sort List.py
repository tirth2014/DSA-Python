# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution - 1 (Naive)
# Gives TLE for big input and also this is invalid approach. We shouldn't extract ll values in a simple list and then sort.
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


# Solution - 2 (Merge Sort)
# Time Complexity:  O(n*logn)
# Space Complexity:  O(logn)

from typing import Optional, Any

# Definition for a node of the singly-linked list.
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
      
# Main Problem
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        left = self.sortList(head)  # left half recursive call
        right = self.sortList(mid)  # right half recursive call
        return self.merge_ll(left,right) # merge left and right lists

    def get_mid(self,head):
        # Using 2-pointer approach ( tortoise-hare algorithm )
        slow = fast = head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next       # slow forwards by 1 step
            fast = fast.next.next  # fast forwards by 2 steps
        prev_slow.next = None      # Disconnect first left half with right half
        return slow

    def merge_ll(self,left,right):
        ptr = ListNode(None)
        curr = ptr

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        # For unequal length of left and right ll

        if left:
            curr.next = left

        if right:
            curr.next = right

        return ptr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(9)
    ll.insert_at_end(6)
    ll.insert_at_end(5)
    ll.print_linked_list()
    ob = Solution()
    ll.print_linked_list()
    newhead = ob.sortList(ll.head)
    ll.print_linked_list(newhead)

