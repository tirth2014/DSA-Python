# BRUTE FORCE - O(n^2) in Worst Case - gives TLE
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        n = len(weights)
        minc,maxc = max(weights),total+1
        for c in range(minc,maxc):
            d = 0
            weightsDone = 0
            for w in weights:
                weightsDone += w
                if weightsDone > c:
                    d += 1
                    weightsDone = w
            d += 1
            # If total_days is greater than the given number of days days, it means that we need a higher capacity to ship all
            # the packages within the given number of days. In this case, we increase the current capacity capacity by 1 and
            # repeat the process until we find the minimum capacity required to ship all the packages within days.
            if d <= days:
                return c
            
