# 1. Kadane's Algo:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_till_now = -inf
        curr_max = 0
        for i in range(len(nums)):
            curr_max = max(nums[i], curr_max+nums[i])
            max_till_now = max(max_till_now, curr_max)

        return max_till_now

      
# 2. Divide & Conquer Approach:- O(nlogn) space and O(nlogn) memory

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArray(A,L,R):
            if L > R: return -inf
            mid, left_sum, right_sum,curr_sum = (L+R)//2,0,0,0
            for i in range(mid-1,L-1,-1):
                left_sum = max(left_sum, curr_sum := curr_sum+A[i])
            curr_sum = 0
            for i in range(mid+1,R+1):
                right_sum = max(right_sum, curr_sum := curr_sum+A[i])
            return max(maxSubArray(A,L,mid-1), maxSubArray(A,mid+1,R), left_sum+A[mid]+right_sum)
        return maxSubArray(nums, 0, len(nums)-1)

