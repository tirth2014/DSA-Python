class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.

"""
=> Brute-Force Approach:
Time Complexity
O(n ^ 2), where ‘n’ is the length of the doubly linked list.
We are using two nested loops. The outer loop is running ‘n’ times (compare it to a for loop having ‘i’ from 0 to ‘n’ - 1), and the inner loop is running ‘n’ - ‘i’ times.

So the total number of iterations:

= (‘n’ - 1) + (‘n’ - 2) + (‘n’ - 3) + … + 2 + 1
= (‘n’ - 1) * ‘n’ / 2

Hence the time complexity is O(n ^ 2).

Space Complexity : O(1)
"""
def findPairs(head: Node, k: int) -> [[int]]:
    
    ptr1 = head
    res = []

    while ptr1:
        ptr2 = ptr1.next

        while ptr2:
            curr_sum = ptr1.data + ptr2.data
            if curr_sum == k:
                res.append((ptr1.data, ptr2.data))
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    return res


# Optimized (Hashing)
# Time Complexity :  O(N)
# Space Complexity : O(N)

def findPairs(head: Node, k: int) -> [[int]]:
    
    ptr1 = head
    res = []
    hash_dict = {}

    while ptr1:
        val = ptr1.data
        if (k-val) in hash_dict:
            res.append([val, k-val])
        else:
            hash_dict[val] = 1
        ptr1 = ptr1.next
    
    return res


# Optimal (Two-pointer)
# Time Complexity :  O(N)
# Space Complexity : O(1)

def findPairs(head: Node, k: int) -> [[int]]:
    
    res = []
    start = end = head

    while end and end.next:
        end = end.next
    
    while start != end and end.next != start:
        curr_sum = start.data + end.data
        
        if curr_sum == k:
            res.append((start.data, end.data))
            start = start.next
            end = end.prev
        
        elif curr_sum < k:
            start = start.next
        
        else:
            end = end.prev

    return res
