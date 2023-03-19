# O(NlogN) and O(1)
# No need to find pairs,combinations any such stuff...it's jst a basic problem
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        # jump 2 elements in each iteration
        for i in range(0,len(nums),2):
            max_sum += nums[i]
        return max_sum
      
# 2 Liner:
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0,len(nums),2)])
      
      
# 1 Liner very pythonic 
# The space complexity is O(n) because a new list is created containing every second element of the sorted list.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        

        
      
      
