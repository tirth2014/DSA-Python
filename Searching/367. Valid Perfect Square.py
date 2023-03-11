# Binary Search Approach
# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l <= r:
            m = (l+r)//2
            sq = m*m
            if sq == num:
                return True
            elif num < sq:
                r = m-1
            else:
                l = m+1
        return False
