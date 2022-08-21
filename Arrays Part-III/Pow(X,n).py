#sol-1 (direct approach)

class Solution:
    def myPow(self, x: float, n: int) -> float:
      return x**n
    
# sol-2 -  O(log*n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1
            
            res = helper(x,n//2)
            res = res*res
            return x*res if n%2 else res        # n%2 == 1 means odd
        
        res = helper(x,abs(n))
        return res if n>0 else 1/res
      
        # or
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x: return 0
        if not n: return 1
        
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:                             # n is odd 
            return x*self.myPow(x,n-1)
        else:                               # n is even
            return self.myPow(x*x,n//2)        
