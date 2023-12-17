
import ast
from typing import List


# Time O(N)
# Space O(N)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        # Using prefix sum algorithm
        # This approach works for array with all elements either +ve, -ve etc...
        # at every index if prefix sum is 's', we're looking for
        # no. of subarrays before that element with prefix_sum 's-k'
        # storing 0 in dict/hashmap(pref_sum: cnt) is very important
        # s = prefix sum
        # k = goal
        # dict = prefix sum count dictionary
        dict = {}
        s, res = 0, 0
        dict[0] = 1
        for num in nums:
            s += num
            res += dict.get(s - k, 0)
            dict[s] = dict.get(s, 0) + 1
        return res
      

if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        # arr = list(map(int, input("arr: ").split()))
        arr = ast.literal_eval(input("arr: "))
        # st = input("string: ")
        # num = input("num string: ")
        k = int(input("goal: "))
        ans = ob.numSubarraysWithSum(arr, k)
        print(ans)



# Time O(N)
# Space O(1)
# Sliding Window Solution
class Solution:
    def subarrs_sum_atmost_k(self, nums, k):
        i = j = res = sum_till = 0
        n = len(nums)
        while j < n:
            sum_till += nums[j]
            while i <= j and sum_till > k:
                sum_till -= nums[i]
                i += 1
            res += j-i+1  # Add size(window) in res
            j += 1
        return res

    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        return self.subarrs_sum_atmost_k(nums, k) - self.subarrs_sum_atmost_k(nums, k-1)
