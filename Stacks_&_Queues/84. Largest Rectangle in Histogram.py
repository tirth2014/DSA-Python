# Brute-Force Naive solution
# ~ T.C: O(N*N) 
class Solution:
    def horizontal_rec_area(self, heights, ind):
        cnt = 0

        # left side smaller
        i = ind
        while i >= 0 and heights[i] >= heights[ind]:
            cnt += 1
            i -= 1

        # right side smaller
        i = ind + 1
        while i < len(heights) and heights[i] >= heights[ind]:
            cnt += 1
            i += 1

        return heights[ind] * cnt

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(set(heights)) == 1:
            return heights[0] * len(heights)

        curr_max = float('-inf')

        for ind in range(len(heights)):
            curr_max = max(curr_max, heights[ind], self.horizontal_rec_area(heights, ind))

        return curr_max




# More optimized
# Intuition: Pre-compute left-smaller and right-smaller indices using the concept of the next greater element and the next smaller element. 
# So, we don't need to find separately for each element each time
# We got rid of the "horizontal_rec_area" method
# Time Complexity: O(N)
# Space Complexity: O(3*N) where 3 is for the 1.stack, 2.left_smaller array, and 3.right_smaller array
import ast
from typing import List

# Running Example:
# heights:      [2,1,5,6,2,3]
# left_smaller: [0,0,2,3,2,5]
# left_smaller: [0,5,3,3,5,5]
# max_rec_area: [2,6,10,6,8,3]
# res = 10

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_smaller, right_smaller, res = [0]*n, [n-1]*n, 0

        # Find left smaller boundaries for each element
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                # If there's index on stack top then it's left smaller boundary else 0
                left_smaller[i] = stack[-1] + 1
            stack.append(i)

        # Find right smaller boundaries for each element
        stack = []
        for j in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                # If there's index on stack top then it's right smaller boundary else len(heights)-1
                right_smaller[j] = stack[-1] - 1
            stack.append(j)

        # Find maximum rectangle area
        for idx in range(n):
            rec_area = (right_smaller[idx] - left_smaller[idx] + 1) * heights[idx]
            res = max(res, rec_area)

        return res


if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        # arr = list(map(int, input("arr: ").split()))
        arr = ast.literal_eval(input("arr: "))
        # num = input("num string: ")
        # k = int(input("k: "))
        ans = ob.largestRectangleArea(arr)
        print(ans)
