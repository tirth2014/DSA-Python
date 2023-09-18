# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water
# https://takeuforward.org/data-structure/trapping-rainwater/
# https://www.youtube.com/watch?v=m18Hntz4go8

"""
Brute Force - TLE
If we observe carefully the amount the water stored at a particular index is the min(max_left, max_right) of the index minus the height at that index.

Time Complexity: O(N*N) as for each index we are calculating leftMax and rightMax so it is a nested loop.
Space Complexity: O(1).
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        for i in range(len(height)):
            max_left = max_right = 0
            for l in range(i,-1,-1):
                max_left = max(max_left, height[l])
            for r in range(i, len(height)):
                max_right = max(max_right, height[r])
            trapped += min(max_left, max_right) - height[i]
        return trapped


"""
Solution 2:Better solution

Intuition: 
We are taking O(N) for computing leftMax and rightMax at each index. 
The complexity can be boiled down to O(1) if we precompute the leftMax and rightMax at each index.

Approach: 
Take 2 array prefix and suffix array and precompute the leftMax and rightMax for each index beforehand. 
Then use the formula min(prefix[i], suffix[i])-arr[i] to compute water trapped at each index.

Time Complexity: O(3*N) overall... as we are traversing through the array once and O(2*N) for computing prefix and suffix array.
Space Complexity: O(N)+O(N) for prefix and suffix arrays. ( + another O(N) for stack approach )
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack, trapped, n = [], 0, len(height)
        prev_greatest, next_greatest = [0]*n, [0]*n
        # prev_greatest = next_greatest = [0]*n...this is WRONG!... Here both are referring to same array at same address, so, changing one will result in change in other
        i = n-1
        for i in range(n-1,-1,-1):
            ele = height[i]
            while stack and stack[-1] <= ele:
                stack.pop()
            if stack:
                next_greatest[i] = stack[-1]
            elif not stack:
                next_greatest[i] = ele
                stack.append(ele)
            elif ele > stack[-1]:
                next_greatest[i] = ele
                stack[-1] = ele

        stack = []
        for i, ele in enumerate(height):
            while stack and stack[-1] <= ele:
                stack.pop()
            if stack:
                prev_greatest[i] = stack[-1]
            if not stack:
                prev_greatest[i] = ele
                stack.append(ele)
            elif ele > stack[-1]:
                stack[-1] = ele

        for i in range(n):
            trapped += min(prev_greatest[i], next_greatest[i]) - height[i]

        return trapped


# Using stack is not required for this approach...we can get prefix_max and suffix_max arrays directly  
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped, n =  0, len(height)
        prev_greatest, next_greatest = [0]*n, [0]*n  # prefix_max, suffix_max
        # prev_greatest = next_greatest = [0]*n...this is WRONG!... Here both are referring to same array at same address, so, changing one will result in change in other

        # calculate prefix and suffix arrays
        next_greatest[n - 1] = height[n - 1]
        for i in range(n-2,-1,-1):
            next_greatest[i] = max(next_greatest[i+1], height[i])

        prev_greatest[0] = height[0]
        for i, ele in enumerate(height):
            prev_greatest[i] = max(prev_greatest[i-1], ele)

        # Now, we have left_max and right_max pre-computed...so, we can get them in O(1)
        for i in range(n):
            trapped += min(prev_greatest[i], next_greatest[i]) - height[i]

        return trapped


"""
Solution 3: Optimal Solution (Two pointer approach)
Time Complexity: O(N) because we are using 2 pointer approach.
Space Complexity: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped, n =  0, len(height)
        i, j, left_max, right_max = 0, n-1, height[0], height[n-1]
        while i <= j:
            if height[i] <= height[j]: # This condition makes sure there's building on right (j-th building) with height > this building(i-th)
                if height[i] > left_max:
                    left_max = height[i]
                else:
                    # In Previous approach, we were doing min(left_max, right_max) - height[i]. But here,
                    # We've already made sure there's building on right with height >= left_max..So we don't need right_max now.
                    trapped += left_max - height[i]
                i += 1

            else: # height[j] < height[i]
                # height[j] < height[i] this condition makes sure, there's building on left with at least j-th building's height
                # Because of this condition we won't need to check for left_max
                if height[j] > right_max:
                    right_max = height[j]
                else:
                    trapped += right_max - height[j]
                j -= 1

        return trapped
