# Linear search - O(n)

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i<=x:
            j = i+1
            if i*i <= x and j*j > x:
                return i
            i+=1
            
#  Binary search - O(logn)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left,right = 1, x
        while left <= right:
            mid = (left+right)//2
            
            if x == mid ** 2:
                return mid
            elif x > mid**2:
                left=mid+1
            else:
                right=mid-1
        return min(left,right)
      
# Newton Raphson Formula -  O(1)
# Intuition: finding sqaure root of a is identical to finding roots of quadtratic polynomial x^2 - a = 0.
# randomly choose a point, find the slope there and see where its intersect the x axis, then repat again.

# the time complexity of calculating a root of a function f(x) with n-digit precision, provided that a good initial approximation is known, is O((log n)F(n)) where F(n) is the cost of calculating f(x)/f'(x) with n-digit precision.
# here we used 20 loops to converge to a solution no matter the inputs, assuming F(n) also constant

class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        for _ in range(20):
            temp = res
            res = temp - (temp*temp-x)/(2*temp)
        return math.floor(res)
