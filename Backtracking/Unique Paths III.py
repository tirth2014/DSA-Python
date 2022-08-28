# Backtracking + DFS
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        start = end = None
        empty = 0                       # TO STORE COUNT OF NON-OBSTACLE SQUARES

        for i in range(m):
            for j in range(n):
                empty += grid[i][j] == 0
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)       
                    
        visited = set()
        self.result = 0
        def dfs(r,c,visited,walk):
            if (r,c) == end:
                if walk == empty+1:         # TO VERIFY IF ALL NON-OBSTACLE SQUARES ARE VISITED EXACTLY ONCE 
                    self.result += 1
                return 
            if 0<=r<m and 0<=c<n and grid[r][c] != -1 and (r,c) not in visited: 
                visited.add((r,c))
                for i,j in ((0,-1),(0,1),(-1,0),(1,0)):
                    dfs(r+i,c+j,visited,walk+1)
                visited.remove((r,c))
        dfs(start[0],start[1],visited,0)
        return self.result
      
# Time Complexity: O(3^m*n) because on each step (except first) we have no more than 3 options to go: all directions except direction we came from. In practice however it will work much faster than this estimate because of big number of dead-ends  
# Space complexity: O(mn)
