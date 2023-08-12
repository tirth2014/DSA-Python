"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
"""
Time Complexity:
The main contributor to the time complexity is the backtrack function, which is called recursively. 
In the worst case, for each position in the permutation, we have to check all elements of nums to determine which element can be placed at that position. 
Since we have n positions to fill and n elements in nums, the worst-case time complexity is O(n!).
"""
import ast
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ds=[]):
            if len(ds) == len(nums):
                res.append(ds[:])
                return

            for i in range(len(nums)):
                print('nums[i]: %s, ds: %s' %(nums[i], ds))
                if nums[i] not in ds:
                    ds.append(nums[i])
                    print('ds',ds)
                    backtrack(ds)
                    popped = ds.pop()
                    print('popped',popped)

        backtrack()
        return res
    

if __name__ == '__main__':
    ob = Solution()
    # i1 = str(input("enter s: "))
    i2 = input("enter nums list: ")
    i2 = ast.literal_eval(i2)
    print("i2: ",i2)
    ans = ob.permute(i2)
    print(and)


# A little optimized approach
# As set has O(1) lookup time while list has O(N) lookup time in avg. case
# set() is an unordered data structure so, directly using it will give a wrong answer as the order is not preserved.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(ds=[]):
            if len(ds) == len(nums):
                res.append(ds[:])
                return

            for i in range(len(nums)):
                if nums[i] not in used:
                    ds.append(nums[i])
                    used.add(nums[i])
                    backtrack(ds)
                    ds.pop()
                    used.remove(nums[i])
        backtrack()
        return res

# Optimized space complexity by avoiding the use of ds list and instead passing the current index to the backtrack function 
# to keep track of the position being filled. This way, we can modify the input list in place and backtrack to its previous state without the need for additional space.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ind=0):
            if ind == len(nums):
                res.append(nums[:])
                return

            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]  # Swap elements
                backtrack(ind + 1)  # Move to the next position
                nums[i], nums[ind] = nums[ind], nums[i]  # Backtrack (swap back)

        backtrack()
        return res

# For understanding flow [from 1st approach]
enter nums list: [1,2,3]
i2:  [1, 2, 3]
nums[i]: 1, ds: []
ds [1]
nums[i]: 1, ds: [1]
nums[i]: 2, ds: [1]
ds [1, 2]
nums[i]: 1, ds: [1, 2]
nums[i]: 2, ds: [1, 2]
nums[i]: 3, ds: [1, 2]
ds [1, 2, 3]
popped 3
popped 2
nums[i]: 3, ds: [1]
ds [1, 3]
nums[i]: 1, ds: [1, 3]
nums[i]: 2, ds: [1, 3]
ds [1, 3, 2]
popped 2
nums[i]: 3, ds: [1, 3]
popped 3
popped 1
nums[i]: 2, ds: []
ds [2]
nums[i]: 1, ds: [2]
ds [2, 1]
nums[i]: 1, ds: [2, 1]
nums[i]: 2, ds: [2, 1]
nums[i]: 3, ds: [2, 1]
ds [2, 1, 3]
popped 3
popped 1
nums[i]: 2, ds: [2]
nums[i]: 3, ds: [2]
ds [2, 3]
nums[i]: 1, ds: [2, 3]
ds [2, 3, 1]
popped 1
nums[i]: 2, ds: [2, 3]
nums[i]: 3, ds: [2, 3]
popped 3
popped 2
nums[i]: 3, ds: []
ds [3]
nums[i]: 1, ds: [3]
ds [3, 1]
nums[i]: 1, ds: [3, 1]
nums[i]: 2, ds: [3, 1]
ds [3, 1, 2]
popped 2
nums[i]: 3, ds: [3, 1]
popped 1
nums[i]: 2, ds: [3]
ds [3, 2]
nums[i]: 1, ds: [3, 2]
ds [3, 2, 1]
popped 1
nums[i]: 2, ds: [3, 2]
nums[i]: 3, ds: [3, 2]
popped 2
nums[i]: 3, ds: [3]
popped 3
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
