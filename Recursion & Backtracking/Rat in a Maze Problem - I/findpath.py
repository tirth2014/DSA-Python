"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:
Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR,
when printed in sorted order we get DDRDRR DRDDRR.
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""


# Time Complexity: O(4^(n*n)), because on every cell we need to try 4 different directions.
# Space Complexity:  O(n*n), Maximum Depth of the recursion tree(auxiliary space).
# Approach with maintaining visited dictionary and writing if condition for each direction
from typing import List
class Solution:
    def findPathHelper(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], path: str, vis: List[List[int]]):
        if i == n - 1 and j == n - 1:
            ans.append(path)
            return


        # downward
        if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, path + 'D', vis)
            vis[i][j] = 0


        # left
        if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, path + 'L', vis)
            vis[i][j] = 0


        # right
        if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, path + 'R', vis)
            vis[i][j] = 0


        # upward
        if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, path + 'U', vis)
            vis[i][j] = 0


    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]


        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", vis)
        return ans  


# Optimized approach: maintaining visited info. in same matrix instead of creating new visited dictionary and using only 1 if condition for all direction combined.
class Solution:
    def findPath(self, m, n):
        ans = []

        def backtrack(row, col, path = ""):
            di = [1, 0, 0, -1]
            dj = [0, -1, 1, 0]
            dir = "DLRU"

            if row == (n - 1) and col == (n - 1):
                ans.append(path[:])
                return True

            for i in range(4):
                next_row = row + di[i]
                next_col = col + dj[i]
                if next_row >= 0 and next_col >= 0 and next_row < n and next_col < n and m[next_row][next_col] == 1:
                    next_path = path + dir[i]
                    cell = m[row][col]
                    m[row][col] = '#'  # Mark current row,col as visited to prevent visiting them again next.
                    backtrack(next_row, next_col, next_path)
                    m[row][col] = cell

        if m[0][0] == 1:
            backtrack(0, 0)
        return ans


if __name__ == '__main__':
    ob = Solution()
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    i1 = int(input("enter n: "))
    print(i1)
    ans = ob.findPath(maze, i1)
    print(ans)
