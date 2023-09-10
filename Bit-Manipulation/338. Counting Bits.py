"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:
0 <= n <= 105
 
Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

# Brute-force - O(N*logN):
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(n+1):
            num = i
            while num:
                ans[i] += num & 1
                num = num//2       # or num = num >> 1
        return ans
      

# linear time O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(n+1):
            ans[i] = ans[i//2] if not i%2 else ans[i//2]+1
        return ans
      

# linear time O(N) - using bit manipulation (fastest)
# No. of 1's for even n is same same as #1's in n//2 just it's left shifted. Ex: 6(110) is 3(011) right-shifted by 1
# And for odd n. #1's is same as #1's in n//2 + 1. Ex:  5(101) is 2(010) right-shifted by one position + 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(n+1):
            ans[i] = ans[i>>1] if not i&1 else ans[i>>1]+1
        return ans
        
