# Faster than 5% submissions:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nn = set(nums)
        max_cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] - 1 not in nn:
                curr_cnt = 1
                j = 1
                while nums[i] + j in nn:
                    curr_cnt += 1
                    j += 1
                max_cnt = max(max_cnt,curr_cnt)
            i += 1
        return max_cnt 
      
# Faster than 99%
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_cnt = 0   
        for x in nums:
            if x-1 not in nums:
                y=x+1
                while y in nums:
                    y+=1
                max_cnt = max(max_cnt,y-x)
        return max_cnt
      
