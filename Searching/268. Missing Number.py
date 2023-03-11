# Brute Force
# Time Complexity = O(n^2)
# Space complexity = O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(0,len(nums)+1):
            if num not in nums:
                return num
              
# HashMap approach
# Time Complexity = O(n)
# Space complexity = O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        present = {}

        for i in nums:
            present[i] = 1
        
        for i in range(len(nums)+1):
            if i != 0 and i not in present :
                return i
        return 0
      
# Sorting + Binary Search  
# Time Complexity = O(nlogn + logn)
# Space complexity = O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        nums.sort()
        while l <= r:
            m = (l+r)//2
            if m > len(nums)-1:
                return m
            elif m != nums[m] and m < len(nums):
                r = m-1
            elif m == nums[m]:
                l = m+1
        return l
      
# Gaussian Sum Formula:
# can cause integer overflow as sum value can get very big
# Time Complexity = O(n)
# Space complexity = O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = n*(n+1)/2
        curr_sum = sum(nums)
        return int(actual_sum - curr_sum)
      
# XOR Bit Manipulation
# Time Complexity = O(n)
# Space complexity = O(1)
# No Overflow problem.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        missing = len(nums)

        for i,num in enumerate(nums):
            missing ^= i^num
            # the XOR operation will cancel out any repeated numbers in the array and leave us with the missing number.
            # xor is cumulative means order of operation doesn't matter jst like addition and multiplication
        
        return missing      
