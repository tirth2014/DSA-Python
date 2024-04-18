import ast
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Node constructor with a value, and optional left and right children.
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(tree_list):
    # If the list is empty or starts with None, the tree cannot be created.
    if not tree_list or tree_list[0] is None:
        return None

    # The first item in the list becomes the root of the tree.
    root = TreeNode(tree_list[0])
    # A queue to keep track of nodes to which we need to attach children.
    queue = [root]
    # Start from the second item in the list (index 1) because the root is already used.
    i = 1

    # Process nodes in the queue and assign their children until all elements are used.
    while i < len(tree_list) and queue:
        # Pop the first node from the queue to work on.
        current_node = queue.pop(0)

        # If the current element is not None, create a left child for the current node.
        if tree_list[i] is not None:
            current_node.left = TreeNode(tree_list[i])
            # Add the left child to the queue to process its children later.
            queue.append(current_node.left)
        i += 1  # Move to the next element in the list.

        # Check if there are more elements to process and if the current one is not None.
        if i < len(tree_list) and tree_list[i] is not None:
            # Create a right child for the current node.
            current_node.right = TreeNode(tree_list[i])
            # Add the right child to the queue to process its children later.
            queue.append(current_node.right)
        i += 1  # Move to the next element in the list.

    # Return the root of the fully constructed tree.
    return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            
            node_val = node.val
            lh = helper(node.left)
            rh = helper(node.right)
            self.res = max(self.res, lh + rh + node_val)

            return max(lh + node_val, rh + node_val)

        helper(root)
        return self.res


if __name__ == '__main__':
    ob = Solution()
    # Example usage:
    # tree_list = [1, 2, 2, 3, 3, None, None, 4, 4]
    tree_list = [-10,9,20,None,None,15,7]
    root = create_binary_tree(tree_list)
    ans = ob.maxPathSum(root)
    print('\nans', ans)
