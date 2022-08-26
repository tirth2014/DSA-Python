# Both solutions - O(N) time O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1,cnt2,candidate1,candidate2 = 0,0,0,1
        
        for n in nums:
            if candidate1 == n:
                cnt1+=1
            elif candidate2 == n:
                cnt2+=1
            elif not cnt1:
                candidate1,cnt1 = n, 1
            elif not cnt2:
                candidate2,cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        return [n for n in (candidate1,candidate2) if nums.count(n) > len(nums)//3]
      
# Using Counter:
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        
        return [n for n in ctr if nums.count(n) > len(nums)/3]
      
 # This Can be generalized to k and will take O(kN) time and O(k) space 
