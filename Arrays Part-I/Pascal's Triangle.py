# Solution - 1

class Solution:
    def generate(self, numRows):
        pascal_tri = []
        pas_row = []
        pascal_tri.append([1])

        for row in range(1,numRows):
            for col in range(row + 1):
                if col == 0:
                    cell_val = pascal_tri[row - 1][col]
                    pas_row.append(cell_val)
                if col == row:
                    cell_val = pascal_tri[row - 1][col - 1]
                    pas_row.append(cell_val)
                elif col != row and col != 0:
                    cell_val = pascal_tri[row - 1][col] + pascal_tri[row - 1][col - 1]
                    pas_row.append(cell_val)
            pascal_tri.append(pas_row)
            pas_row = []

        return pascal_tri
      
      # Solution - 2

class Solution:
  def generate(self, numRows):
    res = [[1]]

    for i in range(1, numRows):
        temp1 = res[-1] + [0]
        temp2 = [0] + res[-1]

        res.append([temp1[i]+temp2[i] for i in range(len(temp1))])

    return res
