# Collections -  O(n) , S.C: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = collections.Counter(nums)
        return max(res, key = lambda x: res[x])
      
# Using Dictionary or Hashmap - T.C: O(n)  S.C: O(n) 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
            if d[n] > len(nums)//2:
                return n
              
# Moore's Voting Algorithm  -  T.C: O(n)  S.C:  O(1) 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = 0
        cnt = 0
        for n in nums:
            if not cnt:
                ele = n          
            if ele == n:
                cnt += 1       
            else:
                cnt -= 1
        return ele              
