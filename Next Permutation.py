from itertools import permutations
import sys
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        # 1. Find longest non-increasing(decreasing) suffix
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        pivot = i - 1

        # 2. Find rightmost successor to pivot in the suffix & swap with pivot:
        # while j != pivot:
        #     if nums[j] > nums[pivot]:
        while nums[j] <= nums[pivot]:
            j -= 1
        nums[j], nums[pivot] = nums[pivot], nums[j]

        # 3. Reverse the suffix:
        nums[i:] = nums[len(nums) - 1:pivot:-1]
        
        
        
# Method 2
            
        num = int(''.join(map(str, nums)))
        nums = list(permutations(nums))
        low_num = sys.maxsize
        res = 0
        checked = False
        for i in nums:
            if not checked:
                if int(''.join(map(str, list(i)))) > num:
                    res = int(''.join(map(str, list(i))))
                    checked = True
            if int(''.join(map(str, list(i)))) != num:
                res = min(res, int(''.join(map(str, list(i)))))
            low_num = min(low_num, int(''.join(map(str, list(i)))))

        if res != 0:
            nums = [int(d) for d in str(res)]
        else:
            nums = [int(d) for d in str(low_num)]
        
