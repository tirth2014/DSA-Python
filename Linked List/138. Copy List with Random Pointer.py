# Hash Map Approach:
# Time Complexity  : O(2*N) ~ O(N)   ...linear time
# Space Complexity : O(N)            ...linear space

import ast
from typing import Optional, Any, List


# Definition for node of singly-linked list.
class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    # Special insertion at end method which handles adding of random pointer also
    # Just pass in the list of lists and it'll magically generate a linked list from it with all pointers.
    def insert_at_end(self, ll: List) -> None:
        node_ind_mapping = {}
        temp = self.head
        for ind, lst in enumerate(ll):
            val = lst[0]
            new_node = ListNode(val)
            if not self.head:
                self.head = new_node
                temp = self.head
            temp.next = new_node
            new_node.next = None
            new_node.random = None
            temp = new_node
            node_ind_mapping[ind] = temp
        temp = self.head
        for lst in ll:
            if lst[1] in node_ind_mapping:
                temp.random = node_ind_mapping[lst[1]]
            temp = temp.next


    def print_linked_list(self, head=None):
        temp = head if head else self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

# Main Logic
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # No need to do anything when head is NULL
        if not head:
            return head

        nodes_mapping = {}
        temp = head
        new_head = ListNode(head.val)
        new_tmp = new_head

        # Create new linked list and maintain nodes_mapping dictionary
        while temp:
            nodes_mapping[temp] = new_tmp
            temp = temp.next
            new_tmp.next = ListNode(temp and temp.val) if temp else None
            new_tmp = new_tmp.next

        # Traverse again and add random pointer from "nodes_mapping" dictionary
        tmp, new_tmp = head, new_head
        while new_tmp:
            new_tmp.random = nodes_mapping[tmp.random] if tmp.random else None
            tmp, new_tmp = tmp.next, new_tmp.next

        return new_head


if __name__ == '__main__':
    ll = LinkedList()
    # sample input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    user_input = input("Enter original linked list of nodes,random ptr: ")
    input_lst = user_input.replace('null', 'None')
    input_lst = ast.literal_eval(input_lst)
    ll.insert_at_end(input_lst)
    ll.print_linked_list()
    ob = Solution()
    newhead = ob.copyRandomList(ll.head)
    ll.print_linked_list(newhead)




# Optimal Solution:
"""
Steps:
1. Create new linked list & Attach nodes of new ll to original ll nodes next
2. Deal with random pointers 
3. Separate out original and new ll

# Time Complexity  : O(3*N) ~ O(N)  ...linear time
# Space Complexity : O(1)           ...constant space
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # No need to do anything when the head is NULL
        if not head:
            return head
        temp = head

        # Create a new linked list and also attach deep copy nodes next to their original nodes.
        while temp:
            temp_nxt = temp.next
            temp.next = ListNode(temp and temp.val) if temp else None
            temp.next.next = temp_nxt
            temp = temp_nxt

        # Step 2: Point random pointers in new list
        temp = head
        while temp:
            temp.next.random = temp.random.next if temp.random else None  # temp.next is deep copy node of temp
            temp = temp.next.next                                         # move temp to next original node

        # Step 3: Separate out original and new linked lists
        temp = head
        new_head = head.next
        while temp:
            copy_node = temp.next
            temp.next = copy_node.next              # make temp point to next original node instead of it's copy node
            copy_node.next = copy_node.next.next if copy_node.next else None    # make copy node point to next copy node instead of next original node
            temp = temp.next                        # the next original node will be temp now

        return new_head
