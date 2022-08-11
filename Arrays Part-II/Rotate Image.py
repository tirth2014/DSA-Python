# Solution -1 : Reverse a matrix & then Transpose it.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Reverse a matrix
        matrix[:] = matrix[::-1]   # or  matrix.reverse()
        
        # Transpose a matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

 
# Solution-2 : Most pythonic!

class Solution:
    def rotate(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))
        
    # Note:  * is a splat operator and is used for unpacking list. ex.  func(*[1,2,3]) = func(1,2,3)
# zip(*matrix) is the same as calling zip([1, 2, 3], [4, 5, 6],[7, 8, 9,])
# It will yield:

#       (1, 4, 7)
#       (2, 5, 8)
#       (3, 6, 9)
                
