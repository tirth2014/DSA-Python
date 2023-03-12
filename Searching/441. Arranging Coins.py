# Brute Force
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        row_cnt,i = 0,1
        while i <= n:
            if n >= i:
                n -= i
                row_cnt += 1
                i += 1
            else:
                break
        return row_cnt
     
'''
    Simple Binary Search
    Time Complexity: O(logn)
    Space Complexity: O(1)
    Note: Order of operation matters in python ...left + (right-left) // 2 here for example in   3 + 0 // 2  != 1  but the result is 3 
    as 0//2 is evaluated first = 0 and then 3+0 = 3 (final result)
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n
        while l<=r:
            m = l+(r-l)//2
            coins_used = m*(m+1)//2
            if coins_used == n:
                return m
            elif coins_used < n:
                l = m+1
            else:
                r = m-1
        return r
        
'''
    Optimized Binary Search
    Time Complexity: O(log(N/2)). In case of max.int, time complexity can maximum be O(30) = O(1)
    Space Complexity: O(1)
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n==1 or n==2:
            return 1
        elif n==3:
            return 2

        # Binary Search space will start from 2 to n/2.
        # Number of complete rows cannot be more than n/2
        left,right = 2,n//2
        while left <= right:
            mid = left + (right-left) // 2
            coins_used = mid*(mid+1)//2
            if coins_used == n:
                return int(mid)
            elif coins_used > n:
                right = mid-1
            else:
                left = mid+1

        # Since at this point left > right, left will start pointing to a value greater
        # than the desired result. We will return right as it will point to the correct int value.
        return int(right)

                
