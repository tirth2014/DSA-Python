class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m =len(matrix)
        n = len(matrix[0])
        # first check if first row or col has zero: 
        first_row_zero, first_col_zero = False, False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_zero = True
                    if col == 0:
                        first_col_zero = True
                    matrix[0][col] = matrix[row][0] = 0
                    
        # Now iterate over all rows,cols except first row,col to mark the cell if it's in zero row or zero col :
        for row in range(1,m):
            for col in range(1,n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # Now Check if first_row or first_col is True:
        
        if first_row_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_zero:
            for row in range(m):
                matrix[row][0] = 0
        
        
        # O(m+n) Space solution:-
         
        #         rows, eles = [], []
        #         for row in range(m):
        #             for ele in range(n):
        #                 if matrix[row][ele] == 0:
        #                     rows.append(row)
        #                     eles.append(ele)

        #         for row in range(m):
        #             for ele in range(n):
        #                 if row in rows or ele in eles:
        #                     matrix[row][ele] = 0
