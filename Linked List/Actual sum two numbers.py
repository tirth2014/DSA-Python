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

    def LL_len(self,l1,l2):
        l1_len = l2_len = 0
        while l1 or l2:
            if l1:
                l1 = l1.next
                l1_len += 1
            if l2:
                l2 = l2.next
                l2_len += 1
        return l1_len, l2_len

    def make_len_equal(self,l1,l2):
        l1_len, l2_len = self.LL_len(l1, l2)
        len_diff = abs(l1_len - l2_len)
        temp = l2 if l1_len > l2_len else l1  # Assign smaller LL's head node in temp
        for _ in range(len_diff):
            node = ListNode(0)
            node.next = temp
            temp = node
        if l1_len > l2_len:
            l2  = temp
        else:
            l1 = temp
        return l1, l2  

    def add2_recurse(self, l1, l2,new_head):
        if not l1.next and not l2.next:
            new_sum = l1.val + l2.val
            carry = new_sum // 10
            node = ListNode(new_sum % 10)
            new_head.next = node
            return carry, new_head

        carry, new_head = self.add2_recurse(l1.next, l2.next, new_head)

        new_sum = carry + l1.val+ l2.val
        n_carry = new_sum // 10
        node = ListNode(new_sum % 10)
        nxt = new_head.next
        new_head.next = node
        node.next = nxt
        return n_carry, new_head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        l1, l2 = self.make_len_equal(l1, l2)  # Make both linked lists length equal by pre-padding 0's in smaller LL.
        new_node = ListNode(None)
        carry,new_head = self.add2_recurse(l1,l2,new_node)  # Call recursive function to get sum of numbers represented by l1 and l2
        if carry:
            new_head.val = carry
            return new_head
        return new_head.next   # Return new resultant linked list's head node


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(0)
    l1.insert_at_end(9)
    l1.print_linked_list()

    l2 = LinkedList()
    l2.insert_at_end(9)
    l2.print_linked_list()

    ob = Solution()
    newhead = ob.addTwoNumbers(l1.head, l2.head)
    l1.print_linked_list(newhead)
