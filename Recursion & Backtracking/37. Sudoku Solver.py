"""
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
# Time Complexity: O(9^(n^2)), in the worst case, for each cell in the n X n board, we have 9 possible numbers.
# In this problem it's 9^81 in worst case.

# Beats 41.37% of users with Python3 
# Space complexity: Beats 82.30%

import ast
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = range(1,10)
        nums = list(map(str, nums))

        def is_num_valid(num,row=0,col=0):

            # Check if num is already present in the same row
            if any(e == num for e in board[row]):
                return False

            # Check if num is already present in the same column
            if any(row[col] == num for row in board):
                return False

            # Check if num is already present in the current 3 x 3 box
            start_row = (row // 3) * 3  # check it's 0,3 or 6
            start_col = (col // 3) * 3  # check it's 0,3 or 6
          
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if board[i][j] == num:
                        return False

            # The num is valid to enter
            return True

        def dfs():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in nums:
                            if is_num_valid(num, row, col):
                                board[row][col] = num
                                if dfs():
                                    # Sudoku solved successfully
                                    return True
                                board[row][col] = '.'  # backtrack
                        # Not possible to enter any number from 1 to 9. So, return to the previous recursion
                        return False

            # Sudoku solved successfully
            return True

        dfs()
        return board


if __name__ == '__main__':
    ob = Solution()
    i1 = input("enter board: ")
    i1 = ast.literal_eval(i1)
    ans = ob.solveSudoku(i1)
    print('result:', and)



# Beats 50.17% of users with Python3 
# Space complexity: Beats 82.30%

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = range(1,10)
        nums = list(map(str, nums))

        def is_num_valid(num,row,col):

            start_row = (row // 3) * 3  # check it's 0,3 or 6
            start_col = (col // 3) * 3  # check it's 0,3 or 6

            # Optimized by using only 1 for loop to check all the three conditions
            for ind in range(9):
                # Check if num is already present in the same row
                if board[row][ind] == num:
                    return False

                # Check if num is already present in the same column
                if board[ind][col] == num:
                    return False

                # Check if num is already present in the current 3 x 3 box
                if board[(ind//3) + start_row][(ind % 3) + start_col] == num:
                    return False

            # num is valid to enter
            return True

        def dfs():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in nums:
                            if is_num_valid(num, row, col):
                                board[row][col] = num
                                if dfs():
                                    # Sudoku solved successfully
                                    return True
                                board[row][col] = '.'  # backtrack
                        # Not possible to enter any number from 1 to 9. So, return to previous recursion
                        return False

            # Sudoku solved successfully
            return True

        dfs()
        return board

# Few small optimizations to improve the efficiency of code:
# Beats 64.47% of users with Python3      
# Space complexity: Beats 14.50%
# Caching Valid Numbers Check:
# Within the is_num_valid function, we are performing the same validity checks multiple times for different cells in the same row, column, and 3x3 box. 
# We can cache these valid numbers in sets and reuse them to speed up the checking process.  

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_num_valid(num,row,col):
            start_row = (row // 3) * 3  # check it's 0,3 or 6

            return (
                    num not in valid_rows[row] and
                    num not in valid_cols[col] and
                    num not in valid_boxes[start_row + col//3]
            )

        def dfs():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in range(1,10):
                            num = str(num)
                            if is_num_valid(num, row, col):
                                board[row][col] = num
                                valid_rows[row].add(num)
                                valid_cols[col].add(num)
                                valid_boxes[(row//3) * 3 + col//3].add(num)

                                if dfs():
                                    # Sudoku solved successfully
                                    return True

                                valid_rows[row].remove(num)
                                valid_cols[col].remove(num)
                                valid_boxes[row//3 * 3 + col//3].remove(num)
                                board[row][col] = '.'  # backtrack

                        # Not possible to enter any number from 1 to 9. So, return to previous recursion
                        return False

            # Sudoku solved successfully
            return True

        valid_rows = [set() for _ in range(9)]
        valid_cols = [set() for _ in range(9)]
        valid_boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    valid_rows[row].add(num)
                    valid_cols[col].add(num)
                    valid_boxes[3 * (row//3) + col//3].add(num)
        dfs()
        return board
