# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Brute Force approach:

# Take pointer to either headA or headB and for each node traverse all the nodes of other ll to check if both are same and return it if same.
# Time Complexity: O(M * N)
# Space Complexity: O(1)


# Better approach (Hashing):
# Store ListNodes either in set or dictionary as both have avg. lookup time of O(1). 
# But, don't store in list... it's O(N)

# Time Complexity: O(N+M)
# Space Complexity: O(N), where N is the length of first ll A

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None


# Optimal Approach - 1:
# Find the length of both lists.
# Find the positive difference between these lengths.
# Move the dummy pointer of the larger list by the difference achieved. This makes our search length reduced to a smaller list length.
# Move both pointers, each pointing two lists, ahead simultaneously if both do not collide.
# If both collide return that intersecting node
# Time Complexity: O(N+M) + O(abs(N-M)) + O(min(N,M))
# Space Complexity: O(1), where N is the length of first ll A and M is the length of second ll B

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = self.get_ll_len(headA)
        len_B = self.get_ll_len(headB)
        tempA = headA
        tempB = headB
        len_diff = abs(len_A - len_B)
        
        # Move forward longer list pointer by len_diff
        if len_A >= len_B: 
            # List A is longer move it forward to reduce difference
            while len_diff:
                len_diff -= 1
                tempA = tempA.next
        else:
            # List B is longer move it forward to reduce difference
            while len_diff:
                len_diff -= 1
                tempB = tempB.next
              
        # Now move both list pointers 1 step forward till they collide
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
            
        return None

    def get_ll_len(self,head):
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next        
        return cnt


# Optimal Approach - 2
# Take two dummy nodes for each list. Point each to the head of the lists.
# Iterate over them. If anyone becomes null, point them to the head of the opposite lists and continue iterating until they collide.

# Time Complexity: O(2*max(N,M))
# Space Complexity: O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1, t2 = headA, headB    
        while t1 != t2:
            t1 = headB if not t1 else t1.next
            t2 = headA if not t2 else t2.next
        return t1 
