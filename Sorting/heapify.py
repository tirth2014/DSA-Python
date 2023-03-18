class Solution:

    def heapify(self, A):
        # Call heapify_helper starting from first non-leaf node and going in bottom-up fashion in tree.
        # Time Complexity Analysis:
        # The function performs a constant amount of work for each node in the tree, and there are n/2 nodes in the tree. 
        # The loop in the heapify function iterates over n/2 nodes and calls the heapify_helper function, which has a worst-case time complexity of O(log n) due to the recursive calls to itself. 
        # Therefore, the overall time complexity of the heapify function is O(n log n) in the worst case.
        
        # Space Complexity = O(1)
        # since it only uses a constant amount of extra memory to store variables such as n, i, left, right, and smallest. The heapify_helper function uses the call stack to store the recursive function calls, but the maximum depth of the call stack is also O(log n) in the worst case, so the overall space complexity of the heapify function is still O(1).
        
        for i in range(len(A) // 2 - 1, -1, -1):
            self.heapify_helper(A, i)

    def heapify_helper(self, A, i):
        # Worst Case time complexity O(NlogN) beacuse of call stack required for recursive calls.
        smallest = i

        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(A) and A[l] < A[smallest]:
            smallest = l

        if r < len(A) and A[r] < A[smallest]:
            smallest = r

        if smallest != i:
            A[smallest], A[i] = A[i], A[smallest]
            self.heapify_helper(A, smallest)


ob = Solution()
arr = [10, 9, 8, 7]
ob.heapify(arr)   # same as heapq.heapify(arr)
print(f'----------The result is======>>>>>>{arr}')
