
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
