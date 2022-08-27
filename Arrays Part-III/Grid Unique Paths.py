# My approach : O(m*n) time & O(m*n) space

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 == n: return m
        paths = [[0 for _ in range(n)] for _ in range(m)]   # Initialize a m x n matrix
        for i in range(n-1):
            paths[m-1][i] = 1  # Only 1 way to reach end from last row cells
        for j in range(m-1):
            paths[j][n-1] = 1  # Only 1 way to reach end from last column cells
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                 paths[i][j]=paths[i+1][j]+paths[i][j+1]  # No. of unique paths from other grid cells = sum of right cell paths + bottom cell paths
        return paths[0][0]     # Return the total number of ways to reach the target

# DP Memoization (Top Down)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i,j):
            if i>=m or j>=n:           return 0
            if i == m-1 and j == n-1:   return 1
            return dfs(i+1,j) + dfs(i,j+1)
        return dfs(0,0)
    
# Time Complexity : O(m*n), the answer to each of cell is calculated only once and memoized. There are m*n cells in total and thus this process takes O(m*n) time.
# Space Complexity : O(m*n), required to maintain dp.

# DP Tabulation (Bottom Up)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)]
        for i,j in product(range(1,m), range(1,n)):          # Iterate over cartesian product of given iterable i.e. matrix - itertools.product()
            dp[i][j] = dp[i-1][j] + dp[i][j-1]              # Current cell = top cell + left cell
        return dp[-1][-1]                                   # Return the last cell
    
# Time Complexity : O(m*n), we are computing dp values for each of the m*n cells from the previous cells value. Thus, the total number of iterations performed is requires a time of O(m*n)
# Space Complexity : O(m*n), required to maintain dp table.

# Space optimized DP 
# O(m*n)  O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(2)]
        for i,j in product(range(1,m), range(1,n)):          # Iterate over cartesian product of given iterable i.e. matrix
            dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1]              # Current cell = top cell + left cell
        return dp[(m-1)&1][-1]                                   # Return the last cell

# Because we don't need the entire matrix, only the current and previous rows, so we maintain 2 rows only of size n and use '&' operator.

# Further improvement - We don't need entire row...only the current column(j) and previous column(j-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _,j in product(range(1,m),range(1,n)):
            dp[j] += dp[j-1]
        return dp[-1]
# Using Math - Combinatorics 

#Time Complexity : O(m+n)
# Space Complexity : O(1)
#Start from (0,0) and go to (m-1, n-1) cell. 
# We need to make (m-1) Down-moves and (n-1) Right-moves to reach the target cell. Total of m+n-2 moves.
# At each cell along the path we can either move down or right. So, we need to find number of unique combinations of these choices.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)
