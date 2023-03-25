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
            
# USING BINARY SEARCH            
"""
In each iteration of the binary search, the code chooses the middle element between the left and right boundaries as the current weight capacity. 
Then, it checks if all the packages can be shipped within the given number of days with the current weight capacity by looping over all the packages and calculating the total weight of packages that can be shipped on each day. 
If the total weight of packages on any day exceeds the current weight capacity, the code increases the number of days required to ship the packages and resets the total weight of packages on the current day to the weight of the current package.

If the number of days required to ship the packages with the current weight capacity is less than or equal to the given number of days, 
the code updates the right boundary of the binary search to the current weight capacity[ TO  CHECK IF IT'S STILL POSSIBLE TO SHIP ALL THE PACKAGES WITH STILL LESS CAPACITY ]. Otherwise, the code updates the left boundary of the binary search to the current weight capacity + 1.

The binary search terminates when the left and right boundaries meet. 
At this point, the left boundary represents the minimum weight capacity required to ship all the packages within the given number of days. 
The code returns the left boundary as the result.

Time Complexity: O(N*log(total)), where N is the number of packages and total is the sum of weights. 
The algorithm performs binary search over the range of possible weight capacities, and for each capacity, it loops over all the packages to check if they can be shipped within the given number of days. The binary search takes O(log(total)) iterations, and for each iteration, the algorithm checks all the packages, which takes O(N) time. Therefore, the overall time complexity is O(N * log(total)).

Space Complexity: O(1) 
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # set left and right boundaries of binary search as the minimum and maximum possible capacity 
        left,right = max(weights),sum(weights)+1

        while left < right:
            # choose the middle element as the current capacity for the ship
            mid = left + (right-left)//2   # mid = current_capacity
            d = 1
            cur = 0 
            for w in weights:
                # add current package weight to current weight
                cur += w
                # if the weight of the current package exceeds the current capacity,
                # reset the current weight to the weight of the current package
                # and increase the number of days required to ship the packages
                if cur > mid:
                    cur = w
                    d += 1
                    if cur>mid or d > days: break
            if d <= days: right = mid
            else: left = mid+1

        # Return the minimum weight capacity required to ship all the packages within the given number of days represented by left boundary of binary search.
        return left

                    

                    
            
            
# Apply our binary search template:

class Solution:
    def shipWithinDays(self, weights: List[int], d: int) -> int:
        
        def feasible(capacity): # Condition function
            cur_days = 1
            cur_weight = 0
            for w in weights:
                cur_weight += w
                if cur_weight > capacity:  # the current shipment of packages is too heavy, wait for the next day
                    cur_weight = w
                    cur_days += 1
                if cur_days > d: return False  # Cannot ship withing d days
            return True

        left,right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left 

                    
            
