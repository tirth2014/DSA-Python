# https://leetcode.com/problems/sliding-window-maximum/

# Naive Brute-force solution
# Find max. element for each window in given array and keep adding it to result.
# T.C: O(N^2)
# S.C: O(K)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_sliding_window = []
        for i in range(n - k + 1):
            max_e = float('-inf')
            for el in nums[i: i+k]:
                max_e = max(max_e, el)
            max_sliding_window.append(max_e)

        return max_sliding_window




# Optimized approach - 1
# Ideally, we want to be able to access the maximum element in less than O(N) time and updating it in less than O(N) time.
# One way to achieve this goal is to push the window elements in a max heap and pop the leftmost (first one of last window) element out of the heap when the window slides.

# T.C: O(N * log(K))
# Iterating through the nums array: This takes O(N) time, as we visit each element once.
# Within the loop, the main operations are performed:
# Adding elements to the max-heap (heapq.heappush): This operation takes O(log(K)) time, where K is the size of the sliding window. 
# In the worst case, it takes logarithmic time to maintain the heap structure.
# Removing elements from the max-heap (heapq.heappop): This operation also takes O(log(K)) time.
# In total, we perform the push and pop operations for each element in the array, resulting in a time complexity of O(N * log(K)).
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []  # min heap, default for heapq
        max_sliding_window = []
        for i, curr in enumerate(nums):
            # Remove elements (out of bound elements) that are no longer in the current window
            while heap and heap[0][1] < i-k+1:
                heapq.heappop(heap)

            # Push the current element along with its index (negated for max-heap behavior)
            heapq.heappush(heap, (-curr, i))

            if i >= k-1:
                max_sliding_window.append(-heap[0][0]) # Negate to get the actual maximum value

        return max_sliding_window



# Most optimal approach
# Larger elements entering window invalidates smaller elements
# A question we can ask ourselves is "do we need to keep all the window elements in our state?".
# An important observation is for two elements arr[left] and arr[right], where left < right, arr[left] leaves the window earlier as we slide. 
# If arr[right] is larger than arr[left], then there is no point keeping arr[left] in our state
# since arr[right] is always gonna be larger during the time arr[left] is in the window. Therefore, arr[left] can never be the maximum.

# Monotonic deque
# Here we introduce an interesting data structure. It's a deque with an interesting property - the elements in the deque from head to tail are in decreasing order (hence the name monotonic).
# To achieve this property, we modify the push operation so that
# Before we push an element 'curr' into the deque, we first pop everything smaller than it out of the deque. This enforces the decreasing order.

# Time Complexity: O(N)
# Space Complexity: O(K)

import ast
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1: 
          return nums
        max_sliding_window, dq = [0]*(n-k+1), deque()

        for i, curr in enumerate(nums):
            # remove numbers out of range k
            if dq and dq[0] <= i-k:
                dq.popleft()

            # remove smaller numbers in k range as they're useless
            while dq and nums[dq[-1]] <= curr:
                dq.pop()

            dq.append(i)

            # start adding to result list after first k numbers
            if i >= k-1:
                max_sliding_window[i-k+1] = nums[dq[0]]

        return max_sliding_window


if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        # arr = list(map(int, input("arr: ").split()))
        arr = ast.literal_eval(input("arr: "))
        # num = input("num string: ")
        k = int(input("k: "))
        ans = ob.maxSlidingWindow(arr, k)
        print(ans)
