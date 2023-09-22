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
