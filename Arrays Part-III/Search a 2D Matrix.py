# Solution-1 [Binary Search]
# Integers in each row are sorted in ascending from left to right.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        for row in matrix:
            if target <= row[-1]:
                r = len(row) - 1
                while l <= r:
                    mid = (l+r)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid-1
                    else:
                        l = mid+1

        return False
