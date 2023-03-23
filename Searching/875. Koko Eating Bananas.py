# BRUTE FORCE - TLE(Time Limit Exceeded) (107/125 testcases passed)
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        for k in range(1,max(piles)+1):
            hrs = 0
            for j in range(len(piles)):
                hrs += math.ceil(piles[j]/k)
                if hrs > h:
                    break
            if hrs <= h:
                return k
            else:
                continue
                
                
# Using BINARY SEARCH
# time complexity =  O(N*log(max(piles)))
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1,max(piles)
        curr_ans = 0
        while left <= right:
            mid = left + (right-left) // 2
            hrs = 0
            for bananas in piles:
                hrs += math.ceil(bananas/mid)
                if hrs>h:
                    break
            if hrs <= h:
                curr_ans = mid
                right = mid-1
            else:
                left = mid+1
            
        return curr_ans
                                
                
                
