"""
992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3

Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""

class Solution:
    # helper function
    def subarrays_with_atmost_k_distinct(self, nums, k):
        # without the below condition, it'll be wrong for the case:
        # nums = [1,2] and k = 1
        if k == 0:  # IMP1
            return 0

        cnt_dict = {}
        n = len(nums)
        i = j = res = 0
        while j < n:
            cnt_dict[nums[j]] = cnt_dict.get(nums[j], 0) + 1
            while i < j and len(cnt_dict) > k:
                cnt_dict[nums[i]] = cnt_dict.get(nums[i], 0) - 1
                if cnt_dict[nums[i]] == 0:  # IMP2 Don't forget this step
                    del cnt_dict[nums[i]]
                i += 1
            res += j-i+1
            j += 1
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrays_with_atmost_k_distinct(nums, k) - self.subarrays_with_atmost_k_distinct(nums, k-1)
