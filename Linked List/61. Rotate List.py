


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
