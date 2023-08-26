# Find length of Loop
# https://www.codingninjas.com/studio/problems/find-length-of-loop_8160455

"""
Time Complexity
O(n), Where ‘n’ is the size of the linked list.
Both the loop detecting cycle and the loop calculating length will not do more than ‘n’ iterations.
Hence the time complexity is O(n).

Space Complexity
O(1)
We are not using any extra space except ‘fast’, ‘slow’ and ‘length’.
Hence the space complexity is O(1).
"""

class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Using cycle_entry pointer

def find_length(entry,slow,cnt):
    # From the cycle starting point loop again till slow pointer reach cycle start point again to find length
    if slow is entry:
        return cnt
    return find_length(entry,slow.next,cnt+1)

def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow = fast = entry = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
        if slow is fast: # Cycle exist
            while entry is not slow:
                entry = entry.next
                slow = slow.next

            return find_length(entry,slow.next,cnt=1)
    return 0


# If cycle exists then slow and fast pointer will meet at ANY node in cycle. 
# So, after they meet...loop any one (either slow or fast pointer) till they meet again in same node to find the length of cycle.
def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            cycle_len = 0
            while True:
                slow = slow.next
                cycle_len += 1
                if slow is fast:
                    break
            return cycle_len
    return 0
