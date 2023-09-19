# https://leetcode.com/problems/sum-of-subarray-minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-o-n-slightly-easier-to-grasp-solution-explained/

# 1. Backtracking.. Wrong when elements not distinct
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        subarrays_min = []
        mod = 1000000007
        def dfs(curr, i):
            if i == len(arr):
                if curr:
                    subarrays_min.append(min(curr))
                return

            # pick
            if not curr or curr[-1] == arr[i-1]:
                curr.append(arr[i])
                dfs(curr, i+1)
                curr.pop()

            # not-pick
            dfs(curr, i+1)

        dfs([], 0)
        return sum(subarrays_min) % mod


# 2. Using nested loops...gives TLE
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        subarrays_min = []
        n = len(arr)
        mod = 1000000007
        for i in range(n):
            for j in range(i, n):
                subarray_min = min(arr[i : j+1])
                subarrays_min.append(subarray_min)

        return sum(subarrays_min) % mod

# 3. Optimal - Using stack

# time O(n)
# space O(n)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sums = [0]*len(arr)
        stack = []
        mod = 10**9+7
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                stack.pop()

            if stack:
                # if there's a lesser number than current on left side of arr,
                # then it's on top of the stack
                j = stack[-1]
                # reuse contribution of lesser and
                # sum subarrays that include nums between current and lesser
                sums[i] = sums[j] + num * (i-j)
            else:
                # just sum all the subarrays that end with current element at index i (i.e. end with num)
                sums[i] = num * (i+1)
            stack.append(i)

        return sum(sums) % mod
