# Sorting + Two pointer - O(n*logn)
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        res = set()
        while i<j:
            res.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(res)
      
# Shorter and using min,max build-in methods of python
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        return len(set([(nums.pop(nums.index(min(nums))) + nums.pop(nums.index(max(nums))))/2 for _ in range(len(nums)//2)]))


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res,n = set(), len(nums)
        return len(set([(nums[i]+nums[n-i-1])/2 for i in range(n//2)]))
      
