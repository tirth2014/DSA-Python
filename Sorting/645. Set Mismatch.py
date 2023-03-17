# Time Complexity =  O(N)
# Space Complexity = O(N)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False]*(n+1)
        for x in nums:
            if seen[x]:
                repeat = x
            seen[x] = True
        
        for x in range(1,n+1):
            if seen[x] == False:
                missing = x
        
        return [repeat,missing]
      
      
"""
A = [1,2,2,4]
curr_sum = 9
actual_sum = 10

curr_sq_sum = 25
actual_sq_sum = 30

x = repeated number
y = missing number

actual_sum = curr_sum - (x+y) ------------ eq(1)
actual_sq_sum = curr_sq_sum - x^2 + y^2
x^2 - y^2 = curr_sq_sum - actual_sq_sum ------ eq(2)
x^2 - y^2 = (x-y)(x+y) -----eq(3)


from eq(1):
x-y = curr_sum - actual_sum
x-y = 9 - 10 = -1

from eq(2):
x^2 - y^2 = 25 - 30 = -5
from eq(3)
x+y =  -5/-1 = 5
so,
x+y-(x-y) = 5-(-1) = 6 = 2y  =>  y=3 [missing] and x=2 [repeated]

Time Complexity =  O(N)
Space Complexity = O(1)

"""

class Solution:
    def findErrorNums(self, A: List[int]) -> List[int]:
        n = len(A)
        actual_sum = n*(n+1)/2
        curr_sum = sum(A)
        actual_sq_sum = (n*(n+1)*(2*n+1))/6
        curr_sq_sum = sum([x*x for x in A])
        # x-y
        alpha = curr_sum - actual_sum
        # x^2 - y^2
        beta = curr_sq_sum - actual_sq_sum
        # x+y
        gamma = beta / alpha
        missing = (gamma - alpha)//2  # y
        repeated = gamma - missing  # x

        return [int(repeated),int(missing)]      
