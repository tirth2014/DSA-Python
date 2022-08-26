# My approach : O(m*n) time & O(m*n) space

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 == n: return m
        paths = [[0 for _ in range(n)] for _ in range(m)]   # Initialize a m x n matrix
        for i in range(n-1):
            paths[m-1][i] = 1  # Only 1 way to reach end from last row boxes
        for j in range(m-1):
            paths[j][n-1] = 1  # Only 1 way to reach end from last column boxes
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                 paths[i][j]=paths[i+1][j]+paths[i][j+1]  # No. of unique paths from other grid boxes = sum of right box paths + bottom box paths
        return paths[0][0]
