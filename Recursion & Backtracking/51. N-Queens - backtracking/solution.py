'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.' * n for _ in range(n)]  # ex: n = 4, board = ['....', '....', '....', '....']

        def isSafe(row,col):
            # Not optimized - O(N) approach
            # WE ONLY NEED TO CHECK LEFT SIDE AS THERE ARE STILL NO QUEENS PLACED ON RIGHT SIDE COLUMNS
            temp_r = row
            temp_c = col

            # CHECK FOR LEFT UPPER DIAGONAL
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q': return False
                row -= 1
                col -= 1

            row = temp_r
            col = temp_c

            # CHECK FOR LEFT SIDE HORIZONTALLY
            while col >= 0:
                if board[row][col] == 'Q': return False
                col -= 1

            row = temp_r
            col = temp_c

            # CHECK FOR LEFT LOWER DIAGONAL
            while row < n and col >= 0:
                if board[row][col] == 'Q': return False
                row += 1
                col -= 1

            # IT'S SAFE TO PLACE QUEEN ON THIS POSITION
            return True

        def backtrack(col=0):
            if col == n:
                ans.append(board[:])
                return

            for row in range(n):
                if isSafe(row,col):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:] # Successfully placed queen on this column
                    backtrack(col+1)  # Check for next column
                    board[row] = board[row][:col] + '.' + board[row][col+1:]  #While returning to previous board positions remove queen from this position

        backtrack()

        return ans  # n = 4, ans = [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]



# Optimized approach:
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.' * n for _ in range(n)]  # ex: n = 4, board = ['....', '....', '....', '....']
        lower_diagonal_placed = {}  # to keep track of queens placed in the lower diagonals
        upper_diagonal_placed = {}  # to keep track of queens placed in the upper diagonals
        left_placed = {}  # to keep track of queens placed in the left horizontal side of the board

        def isSafe(row,col):
            # Optimized approach - O(1) using hashing
            # For optimization we need to observe this pattern: (row-col) is the same for all upper diagonals and 
            # (row+col) is the same for all lower diagonals. So, we can use a dictionary to check if any queen is placed already on diagonal
            # similarly we can use a dictionary to check for the left horizontal side as the row is the same
            # We only need to check the left side as there are no queens placed on the right side columns yet.

            # CHECK FOR LEFT UPPER DIAGONAL
            if upper_diagonal_placed.get(row-col):
                return False

            # CHECK FOR LEFT SIDE HORIZONTALLY
            if left_placed.get(row):
                return False

            # CHECK FOR LEFT LOWER DIAGONAL
            if lower_diagonal_placed.get(row+col):
                return False

            # IT'S SAFE TO PLACE QUEEN ON THIS POSITION
            return True

        def backtrack(col=0):
            # Recursive function to place queens on the board column by column
            if col == n:
                ans.append(board[:])
                return

            for row in range(n):
                if isSafe(row,col):
                    # If it's safe to place a queen at position (row, col), mark the cell with 'Q' and update the dictionaries
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    upper_diagonal_placed[row-col] = True # All left upper diagonals will have the same (row-col)
                    left_placed[row] = True
                    lower_diagonal_placed[row+col] = True # All left lower diagonals will have same (row+col)

                    # Move to the next column (recursively)
                    backtrack(col+1)

                    # Backtrack by undoing the changes made to the board and dictionaries to explore other possibilities
                    upper_diagonal_placed[row-col] = False
                    left_placed[row] = False
                    lower_diagonal_placed[row+col] = False
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

        # Start the backtracking process from the first column (column 0)
        backtrack()

        return ans  # n = 4, ans = [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]
