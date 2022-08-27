# Problem Statement:
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Solution-1 [Brute Force] 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        @cache
        def dfs(i,j):
            if i>=m or j>=n or obstacleGrid[i][j] == 1:     return 0
            if i == m-1 and j == n-1:   return 1
            return dfs(i+1,j) + dfs(i,j+1)
        return dfs(0,0)

# T.C : O(2^(m*n)) as there're m*n cells, each having 2 possibilities, either Obstacle or No obstacle

# DP memoization (Top-down) - recursions
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        
        def solve(i,j):
            if i>=m or j>=n or obstacleGrid[i][j] == 1: 
                return 0
            
            if i == m-1 and j == n-1: 
                return 1
            
            if dp[i][j] != -1: 
                return dp[i][j]
            
            dp[i][j] = solve(i+1,j) + solve(i,j+1)
            return dp[i][j]
        
        return solve(0,0)
    
# T.C = S.C = O(m*n)            
        
# DP tabulation (bottom-up) - iterations
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])     
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1        
        for i in range(1,m):   # For first column
            dp[i][0] = dp[i-1][0] * (1-obstacleGrid[i][0])            
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] * (1-obstacleGrid[0][j])        
        for i,j in product(range(1,m), range(1,n)):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1-obstacleGrid[i][j])   
        return dp[-1][-1]
        
    
# T.C = S.C = O(m*n)            
        
# in-place
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        obstacleGrid[0][0] = 1-obstacleGrid[0][0]
        for i in range(1,m):   # For first column
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1-obstacleGrid[i][0])
            
        for j in range(1,n):   # For first row
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1-obstacleGrid[0][j])
        
        for i,j in product(range(1,m), range(1,n)):
            obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1-obstacleGrid[i][j])
        
        return obstacleGrid[-1][-1]
        
    
# T.C = O(m*n)            
# S.C = O(1)


     
                
            
        
                
            
