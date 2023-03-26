# The monotonicity of this problem is very clear: 
# if we can make m bouquets after waiting for d days, then we can definitely finish that as well if we wait more than d days.

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(D: int) -> bool: # Condition Function
            bqt_cnt,flwr_cnt = 0,0
            for bloom in bloomDay:
                if bloom > D:
                    flwr_cnt = 0
                else:
                    bqt_cnt += (flwr_cnt+1)//k    # If flower count + 1 == k then bqt++
                    flwr_cnt = (flwr_cnt + 1) % k # If flowers + 1 is not divisible by k, it means that the number of flowers is not enough to make a complete bouquet yet. 
                                                  # So, the remainder is stored as the number of flowers that are yet to bloom for the next bouquet.

                                                  # For example, suppose k is 3, and flowers is currently 1. Then, flowers + 1 would be 2. 
                                                  # Since 2 is not divisible by 3, the remainder, which is 2, is stored as the number of flowers that are yet to bloom for the next bouquet.
            return bqt_cnt >= m

        if len(bloomDay) < m*k: return -1   # # only case where it's impossible

        # Main Binary Search
        left,right = 1, max(bloomDay)
        while left < right:
            mid = left + (right-left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1 
        return left




        
