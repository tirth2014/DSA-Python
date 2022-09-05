# Brute Force - O(N^2) time, O(1) space
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    cnt += 1
        return cnt
      
# Optimized - O(N) time, O(N) space
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt += seen[num+k] + seen[num-k]                # Counts numbers with abs. diff. K
            seen[num] += 1
        return cnt
            
