# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Approach-1 [Adaptive Search] - O(m+n)
# Start from bottom left, if target > item then go to right else go up:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = len(matrix)-1, 0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                j+=1   # go to right in same row
            elif target < matrix[i][j]:
                i-=1   # go up in the matrix
       
# Approach - 2   -  O(m*n)      
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)   

# Approach - 3 (Binary Search) - O(m log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target<=row[-1]:
                l,r = 0, len(row) - 1
                while l <= r:
                    mid = l+(r-l)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:     # target is on left side
                        r = mid-1
                    else:                       # target is on right side
                        l = mid+1

        return False    
