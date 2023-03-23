# Search for a peak element in a 2D matrix using SORTING.
"""
Time complexity: O(mn log n), where m and n are the dimensions of the input matrix. 
The algorithm sorts each row of the matrix, which takes O(n log n) time. This is done for each of the m rows, resulting in a time complexity of O(mn log n).
Space complexity: O(n), where n is the length of each row in the input matrix. 
The algorithm only keeps track of the maximum values of each row and the values of the neighboring elements, which requires a constant amount of memory per row. Therefore, the space complexity is O(n).
"""
class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            rs = sorted(mat[i])       
            j = mat[i].index(rs[-1])    # Find max. element index in original row

            bottom = top = left = right = False
            if i < m-1:
                bottom = mat[i+1][j]  
            if i > 0:
                top = mat[i-1][j]
            if j > 0:     
                left = mat[i][j-1] 
            if j < n-1:
                right = mat[i][j+1]

            if rs[-1] > max(filter(lambda x: x is not False, [bottom,top,left,right])):
                return [i,j]
            else:
                continue
                
                
# Search for a peak element in a 2D matrix using BINARY SEARCH.

"""
Time complexity: O(mlog(n)), where m is the number of rows and n is the number of columns in the matrix. 
The binary search algorithm takes O(log(n)) time to find the middle column and the linear search for the largest element in the middle column takes O(m) time. 
Therefore, the total time complexity is O(mlog(n)).

Space complexity: O(1). 
"""
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        start,end = 0, n-1

        while start <= end:   # Binary Search Column Wise
            mid_col = start + (end-start) // 2
            
            # Finding the largest element in the middle Column
            row_ind, currMax = 0,float('-inf')
            for i in range(m):
                if mat[i][mid_col] > currMax:
                    currMax = mat[i][mid_col]
                    row_ind = i
                
            # Checking the adjacent elements:
            isLeftBig = mid_col > start and mat[row_ind][mid_col-1] > mat[row_ind][mid_col]            
            isRightBig = mid_col < end and mat[row_ind][mid_col+1] > mat[row_ind][mid_col]
            
            if not isLeftBig and not isRightBig:
                return [row_ind,mid_col]
            
            elif isLeftBig:
                end = mid_col - 1
            
            else:
                start = mid_col + 1
    


        



            




                        
