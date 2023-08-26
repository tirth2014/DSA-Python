# Naive approach
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        vals = []
        while temp:
            vals.append(temp.val)
            temp = temp.next
        print(vals)
        return vals == vals[::-1]



# Optimal approach
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list and it's methods
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

    def print_linked_list(self,head=None):
        temp = head if head else self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

# Problem
class Solution:
    def reverse_linked_list(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # Core method
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow is now at exact middle of the ll if odd length ll or at the *right side node if even length ll
        # Reverse the right half of the linked list to compare with left half
        # Note we can also re-reverse and make the original list as it is if needed.
        # here the left half of list will be unlinked with reversed second half.
        slow = self.reverse_linked_list(slow)
        # Now, Slow is the last node of linked list and first node of reversed second half of list
        temp = head
        while slow:
            if temp.val != slow.val:
                return False
            temp = temp.next
            slow = slow.next
        return True



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(2)
    # ll.insert_at_end(1)
    ll.print_linked_list() # 1 2 3 2 1
    ob = Solution()
    # i1 = input("enter board: ")
    # i1 = ast.literal_eval(i1)
    # i2 = int(input("Enter k: "))
    # print("i1: ", i1)
    ans = ob.isPalindrome(ll.head)
    print()
    ll.print_linked_list()  # 1 2 3 1 2
    print('\n',ans) # True


# The left half of list will not be unlinked with reversed second half in this approach.
class Solution:
    def reverse_linked_list(self, head):
        # Base Case
        if not head or not head.next:
            return head

        last_node = self.reverse_linked_list(head.next)
        head_next = head.next
        head_next.next = head
        head.next = None
        return last_node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = temp = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Slow is now at middle of the linked list
        # Reverse the right half of the linked list to compare with left half
        slow.next = self.reverse_linked_list(slow.next)  # Assigning reversed second half first node (original ll last node) to slow's next so as to keep it connected.
        slow = slow.next
        while slow:
            if temp.val != slow.val:
                return False
            temp = temp.next
            slow = slow.next
        return True
