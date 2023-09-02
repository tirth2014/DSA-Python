"""
Solution:  Brute Force -> Gives TLE
Approach:  For each k, find the last element from the list. Move it to the first.
Time Complexity  : O(k*N)
Space Complexity : O(1)      
"""

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

    def reverse_ll(self, head):
        temp = None
        nxt = head.next
        while head and head.next:
            head.next = temp
            temp = head
            head = nxt
            nxt = nxt.next
        head.next = temp
        return head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        while k:
            temp = head
            while temp.next.next:
                temp = temp.next
            last = temp.next
            temp.next = None
            last.next = head
            head = last
            k -= 1
        return head


if __name__ == '__main__':
    ll = LinkedList()
    input_string = input("Enter a list of elements separated by spaces or commas: ")
    ip_lst = list(map(int, input_string.replace(',', ' ').split()))
    for ele in ip_lst:
        ll.insert_at_end(ele)
    ll.print_linked_list()
    ob = Solution()
    k = int(input('k: '))
    newhead = ob.rotateRight(ll.head, k)
    ll.print_linked_list(newhead)
    # print('\n', and)




"""
Brute-force Recursive:
Time Complexity  : O(k*N)
Space Complexity : O(N)
where k is the number of rotations and N is the number of nodes in the linked list.
"""
class Solution:

    def rotate_recurse(self, head, prev, curr, k, ll_len):
        if not curr.next:
            ll_len += 1
            if ll_len == k or (k % ll_len == 0):
                return head, 0, ll_len
            curr.next = head
            head = curr
            prev.next = None
            return head, 1, ll_len

        head, cur_k, ll_len = self.rotate_recurse(head, prev.next, curr.next, k, ll_len + 1)
        
        while not curr.next and cur_k < k:
            if cur_k % ll_len == k % ll_len:
                return head, 0, ll_len
            curr.next = head
            head = curr
            prev.next = None
            return head, cur_k + 1, ll_len
        return head, cur_k, ll_len

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur_k = float('-inf')
        while cur_k != 0 and cur_k < k:
            head, cur_k, ll_len = self.rotate_recurse(head, prev=head, curr=head.next, k=k, ll_len=1)
            if cur_k % ll_len == k % ll_len:
                break
        return head




"""
OPTIMAL APPROACH:
Super simple 3 step approach:
    1. Find length of the ll
    2. Last.next = head [ It will make ll circular ]
    3. Make next of (ll_len - k)'th node as head and break the next link of this node. then return head

    Time Complexity  : O(N)
    Space Complexity : O(1)
"""
class Solution:

    # Helper function to calculate the length of the linked list and find its last node
    def _len_and_last(self, head):
        temp = head
        ll_len = 1
        while temp and temp.next:
            temp, ll_len = temp.next, ll_len + 1
        return ll_len, temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Return as it is if it's empty or 1 node linked list
        if not head or not head.next or k == 0:
            return head

        ll_len, last = self._len_and_last(head)
        last.next = head  # Ensure the last node points to the head, creating a circular linked list
        new_last_ind = ll_len - (k % ll_len)  # Calculate the index of the new last node after rotation

        # Traverse the linked list to find the new last node
        temp = head
        for _ in range(new_last_ind-1):
            temp = temp.next

        head = temp.next  # Update the head to the node after the new last node
        temp.next = None  # Set the next pointer of the new last node to None to terminate the list
        return head       # Return the new head of the rotated linked list





"""
Solution:  Optimized Recursion
Time Complexity  : O(N)
Space Complexity : O(N)      
"""
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def recursive_rotate(prev, curr, ll_len):
            nonlocal head, k
            if curr.next:
                recursive_rotate(prev.next, curr.next, ll_len + 1)  # go to next node recursively
            else:                                                   # arrive at the tail (last node), ready to rotate
                k = k % ll_len    # always <= ll_len...avoid unnecessary work

            if k > 0:             # get back to lower level of node, rotate at this level if still rotation work left
                prev.next, curr.next, head, k = None, head, curr, k - 1

        if not head or not head.next or k == 0:
            return head

        recursive_rotate(prev=head, curr=head.next, ll_len=2)

        return head
