# Brute-Force Naive solution
# ~ T.C: O(N*N) 
class Solution:
    def horizontal_rec_area(self, heights, ind):
        cnt = 0

        # left side
        i = ind
        while i >= 0 and heights[i] >= heights[ind]:
            cnt += 1
            i -= 1

        # right side
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
