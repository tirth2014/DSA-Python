"""
In order to find the k-th smallest value in the table, we can design an enough function, 
given an input num, determine whether there're at least k values less than or equal to num. 
The minimal num satisfying enough function is the answer we're looking for. 

Key to binary search is *discovering monotonicity*. In this problem, if num satisfies enough, then of course any value larger than num can satisfy.

Time complexity: O(m log(mn))
Explanation: The binary search is performed on a range of numbers from 1 to m*n, so the search space has size O(mn). 
For each iteration of the binary search, the enough() function is called, which has to go through each row of the mXn multiplication table to count the number of entries less than or equal to the current value of mid. 
Since there are m rows and the maximum number of entries in each row is n, the time complexity of the enough() function is O(m). Therefore, the total time complexity of the algorithm is O(m log(mn)).

Space complexity: O(1).
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(num: int) -> bool:    # Condition function
            cnt = 0
            for val in range(1,m+1):    # we can just go row by row to count the total number of entries less than or equal to input num.            
                add = min(num//val, n)                   
                if add == 0:
                    break     # The value is smaller then num means it won't come in this row of multiplication table.
                cnt += add
            return cnt >= k

        # Binary Search Driver Code
        left,right = 1, m*n   # Search space (1,m*n) as maximum value in mXn multiplication table is m*n
        while left < right:
            mid = left + (right-left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
