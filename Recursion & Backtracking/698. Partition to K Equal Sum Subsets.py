"""
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
import ast
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        # Starting with bigger ones makes it a lot faster. big numbers are the easiest to place.
        # Always start with big numbers for this kind of problems
        nums.sort(reverse=True) # Game Changer 1
        target_sum =  total_sum // k
        subsets_sum = [0]*k

        # Check if the total sum is divisible by k and if any element is larger than the target sum
        if total_sum % k != 0 or max(nums) > target_sum:
            return False

        def backtrack(ind=0):
            # Base case: all elements have been assigned to subsets
            if ind == len(nums):
                # Check if all subsets have sums equal to the target sum
                return all(subsets_sum[i] == target_sum for i in range(k))

            for i in range(k):
                if subsets_sum[i] + nums[ind] <= target_sum:
                    # Pick the current element for the i-th subset
                    subsets_sum[i] += nums[ind]
                    if backtrack(ind+1):
                        return True # Found a valid partitioning
                    # Not-pick: backtrack
                    subsets_sum[i] -= nums[ind]
                # if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game either.
                # Surprisingly, removing of "empty bucket" trick makes it the slowest Python solution.
                if subsets_sum[i] == 0: 
                    break # Game Changer 2

            return False

        return backtrack()


if __name__ == '__main__':
    ob = Solution()
    i1 = input("enter nums list: ")
    i1 = ast.literal_eval(i1)
    i2 = int(input("Enter k: "))
    print("i1: ", i1)
    ans = ob.canPartitionKSubsets(i1, i2)
    print('result:', ans)
