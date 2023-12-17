# Same idea as 930. Binary Subarrays With Sum
# We'll find
# 1. no. of nice subarrays with <= k odd numbers and
# 2. no. of nice subarrays with <= k-1 odd numbers
# In the new method we'll keep incrementing by size of the window (And not by 1) as we want <= k odd nos. not exact k in it.
# So that we don't miss out any subarrays because of j < len(arr) condition. (In case "j" reaches end of an arr but "i" still on the way)
# Imp. note: while i <= j...In this condition '<' alone won't work because for some case it'll count wrong.
# for ex. nums = [2,4,5], k=1
# for second part:  subarrs_atmost_k_odd(nums, k-1), k-1 = 0
# so when at last i will reach 2nd index so, i = j = 2 so, i < j will be wrong but in next line
# res = j-i+1 will add 1 wrongly to the res. even when 5 is odd and k = 0
# so, i <= j will make i = 3 and j = 2 for last condition so, res += 2-3+1 will be -1+1 = 0

class Solution:
    def subarrs_atmost_k_odd(self, nums, k):
        i = j = res = odd_cnt = 0
        n = len(nums)
        while j < n:
            odd_cnt += nums[j] % 2  # If nums[j] odd increment odd_cnt by 1
            while i <= j and odd_cnt > k:
                odd_cnt -= nums[i] % 2  # If nums[i] odd decrement odd_cnt by 1
                i += 1
            res += j-i+1
            j += 1
        return res

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.subarrs_atmost_k_odd(nums, k) - self.subarrs_atmost_k_odd(nums, k-1)
