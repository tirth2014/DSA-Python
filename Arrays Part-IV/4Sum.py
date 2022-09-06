# Solution - 1 (TLE)
from itertools import combinations
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = list(combinations(nums,4))
        res = list(set(map(lambda x: x if sum(x) == target else None, res)))
        ans = []
        for i in res:
            if i:
                ans.append(list(i))
        return ans
     
