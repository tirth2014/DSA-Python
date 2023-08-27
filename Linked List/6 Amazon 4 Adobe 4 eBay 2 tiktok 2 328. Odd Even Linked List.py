# https://leetcode.com/problems/odd-even-linked-list/description/
# Time Complexity of oddEvenList: O(n)
# Space Complexity of oddEvenList: O(1)

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
          

class Solution:
  
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev_o = head # start from index 1 for odd
        curr_o = prev_o and prev_o.next and prev_o.next.next or None

        first_even = prev_e = head.next # start from second node for even and store first_even node so as to connect it with last odd node in the end.
        curr_e = prev_e and prev_e.next and prev_e.next.next or None # second even indexed node in ll

        # group all odd nodes and group all even nodes
        while curr_e or curr_o:
            prev_o.next = curr_o # make prev odd node's next point to next odd node in ll
            prev_e.next = curr_e # make prev even node's next point to next even node in ll

            prev_o = curr_o
            prev_e = curr_e

            curr_o = curr_o and curr_o.next and curr_o.next.next or None  # go to next odd node and None at last
            curr_e = curr_e and curr_e.next and curr_e.next.next or None # go to next even node and None at last

        prev_o.next = None # Make last node of odd nodes group point to None
        prev_o.next = first_even # Connect odd nodes group with even nodes group
        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(1)
    ll.insert_at_end(3)
    ll.print_linked_list()
    ob = Solution()
    ans = ob.oddEvenList(ll.head)
    print()
    ll.print_linked_list()
    print('\n', ans)
