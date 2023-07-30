'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        ind = 0

        def backtrack(row,col,ind):
            # if board[row][col] == word[ind]:
            if ind == len(word): 
                return True
            if row < 0 or row == m or col < 0 or col == n or board[row][col] != word[ind] or board[row][col] == '#': 
                return False

            cell = board[row][col]
            board[row][col] = '#'

            top = backtrack(row-1,col,ind+1)
            bottom = backtrack(row+1,col,ind+1)
            left = backtrack(row,col-1,ind+1)
            right = backtrack(row,col+1,ind+1)

            board[row][col] = cell

            return top or bottom or left or right

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[ind]:
                    if backtrack(i,j,ind):
                        return True
        return False
