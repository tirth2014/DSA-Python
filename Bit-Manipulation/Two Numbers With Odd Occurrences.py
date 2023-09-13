# https://www.codingninjas.com/studio/problems/two-numbers-with-odd-occurrences_8160466?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

from typing import *

class Solution:
    def twoOddNum(self, nums: List[int]) -> List[List[int]]:
        xor_res = 0
        for num in nums:
            xor_res ^= num

        r_set = 0
        while xor_res:
            if xor_res & 1: break
            r_set += 1
            xor_res >>= 1

        xor1 = xor2 = 0
        for num in nums:
            if num & (1 << r_set):
                xor1 ^= num
            else:
                xor2 ^= num

        return max(xor1,xor2), min(xor1,xor2)

twoOddNum = Solution().twoOddNum
