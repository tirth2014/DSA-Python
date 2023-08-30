from typing import Optional, Any

# Definition for node of singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)
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
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Approach - 1:
# 1. Reverse LL
# 2. Add 1 to the number
# 3. Again reverse LL to get incremented original number
# Time Complexity  : O(3N) ~= O(N)
# Space Complexity : O(1)

class Solution:
    def reverse_ll(self,head):
        if not head or not head.next:
            return head

        prev, curr, nxt = None, head, head.next
        while curr and curr.next:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr

    def addOne(self,head: Node) -> Node:
        new_head = self.reverse_ll(head)
        temp = new_head
        carry = 0
        while temp:
            if temp.data < 9:
                temp.data += 1
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next

        head = self.reverse_ll(new_head)
        if carry == 1:
            nn = Node(1)
            nn.next = head
            head = nn
        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(9)
    ll.insert_at_end(9)
    ll.print_linked_list()
    ob = Solution()
    ll.print_linked_list()
    newhead = ob.addOne(ll.head)
    ll.print_linked_list(newhead)
