# Link: https://leetcode.com/problems/sum-of-subarray-ranges

# Brute-Force
# Time Complexity  : O(N^2)
# Space Complexity : O(1)    
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            l, r = nums[i], nums[i]
            for j in range(i, len(nums)):
                l = min(l, nums[j])
                r = max(r, nums[j])
                res += r - l
        return res



        
# Optimal Solution - Using 2 Increasing Monotonous Stack
# Time Complexity  : O(N)
# Space Complexity : O(4*N) ~= O(N)    

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_sums, max_sums = [0]*len(nums), [0]*len(nums)
        min_stack = []
        max_stack = []

        for i, num in enumerate(nums):
            # Minimum of all subarrays ending with num
            while min_stack and nums[min_stack[-1]] > num:
                min_stack.pop()

            if min_stack:
                j = min_stack[-1]
                min_sums[i] = min_sums[j] + (i-j)*num
            else:
                min_sums[i] = num * (i+1)
            min_stack.append(i)

            # Maximum of all subarrays ending with num
            while max_stack and nums[max_stack[-1]] < num:
                max_stack.pop()

            if max_stack:
                j = max_stack[-1]
                max_sums[i] = max_sums[j] + num*(i-j)
            else:
                max_sums[i] = num * (i+1)

            max_stack.append(i)

        return sum(max_sums) - sum(min_sums)




# Same solution using 1 stack and 2 two iterations of nums:
# Time Complexity  : O(2*N) ~= O(N) 
# Space Complexity : O(2*N) ~= O(N)   

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums_lst = [0] * len(nums)
        stack = []

        for i, num in enumerate(nums):
            # Minimum of all subarrays ending with num
            while stack and nums[stack[-1]] > num:
                stack.pop()

            if stack:
                j = stack[-1]
                sums_lst[i] = sums_lst[j] + (i-j)*num
            else:
                sums_lst[i] = num * (i+1)
            stack.append(i)

        stack,res, sums_lst = [], -sum(sums_lst) ,[0] * len(nums)
        for i, num in enumerate(nums):
            # Maximum of all subarrays ending with num
            while stack and nums[stack[-1]] < num:
                stack.pop()

            if stack:
                j = stack[-1]
                sums_lst[i] = sums_lst[j] + num*(i-j)
            else:
                sums_lst[i] = num * (i+1)

            stack.append(i)
        res += sum(sums_lst)
        return res
