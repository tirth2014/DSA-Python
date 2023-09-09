class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        while n != 1:
            if n % 2 != 0: return False
            n = n//2
        return True


# Approach-2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n==0 else n & n-1 == 0
      

# Same:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not(n & n-1)
