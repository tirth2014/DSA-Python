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
    
# Solution - 2:   O(N^3) time 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            target3 = target - nums[i]
            for j in range(i+1,n):
                l,r = j+1,n-1
                target2 = target3 - nums[j]
                while l<r:
                    two_sum = nums[l] + nums[r]
                    if two_sum < target2:
                        l += 1
                    elif two_sum > target2:
                        r -= 1  
                    elif two_sum == target2:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])   # Note: If we append set i.e (quadruplet) then we can directly return set(ans) at the end
                        while l<r and nums[l] == ans[-1][2]:
                            l += 1
                        while l<r and nums[r] == ans[-1][-1]:
                            r -= 1
                while j+1 < n and nums[j+1] == nums[j]:
                    j += 1
            while i+1 < n and nums[i+1] == nums[i]:
                i += 1
        return list(map(list,(set(tuple(sorted(x)) for x in ans)))) # To remove duplicate quadruplets
                                                                    
