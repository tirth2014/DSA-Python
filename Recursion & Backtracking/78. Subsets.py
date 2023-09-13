"""
78. Subsets (Medium)
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# Using For loop and used unordered set to avoid duplicates
# Beats 46.72% of users with Python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(cur=None, ds=[]):
            res.append(ds[:])
            if cur == nums[-1]:
                return

            for i in range(len(nums)):
                if i not in used and not any(used_i > i for used_i in used):
                    ds.append(nums[i])
                    used.add(i)
                    backtrack(nums[i], ds)
                    ds.pop()
                    used.remove(i)

        backtrack()
        return res


# Using for loop + start index 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(ds=[], start=0):
            result.append(ds[:])
            for i in range(start, len(nums)):
                ds.append(nums[i])
                backtrack(ds, i+1)
                ds.pop()

        backtrack()
        return result

# Standard pick/not-pick approach:
# No need of using for loop 
# Beats 78.58% of users with Python3
# Time Complexity: O(2^n)
# Space Complexity: O(n)
import ast
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i=0,ds=[]):
            if i >= len(nums):
                res.append(ds[:])
                return

            # pick
            ds.append(nums[i])
            backtrack(i+1,ds)
            ds.pop()

            # not pick
            backtrack(i+1)


        backtrack()
        return res


if __name__ == '__main__':
    ob = Solution()
    i1 = input("enter nums list: ")
    i1 = ast.literal_eval(i1)
    print("i1: ", i1)
    ans = ob.subsets(i1)
    print('result:', and)
    

# Iterative Approach:
# Beats 83.68% of users with Python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [item+[num] for item in res]
            print(res)
        
        return res
# For understanding iterative approach:
# nums = [1,2,3]
# Stdout
# [[], [1]]
# [[], [1], [2], [1, 2]]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]        


# Bit manipulation approach (Iterative):
# Beats 81.28% of users with Python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # Left shift 1 (01) by n bits
        p = 1 << n  # same as (2**n) or pow(2,n) which is no. of possible subsets for len n list.
        res = [[] for _ in range(p)]
        
        for i in range(p):
            for j in range(n):
                print('i:%s, j: %s, i >> j: %s, (i >> j) & 1: %s' %(i,j,i >> j, (i >> j) & 1))
                if (i >> j) & 1:
                    res[i].append(nums[j])
                    print('res',res)    
        return res

# Stdout for understanding
# nums = [1,2,3]
# i = [0,1,2,3,4,5,6,7]
# j = [0,1,2]
# 8
# i:0, j: 0, i >> j: 0, (i >> j) & 1: 0
# i:0, j: 1, i >> j: 0, (i >> j) & 1: 0
# i:0, j: 2, i >> j: 0, (i >> j) & 1: 0
# i:1, j: 0, i >> j: 1, (i >> j) & 1: 1
# --> append nums[0] = 1 at index i = 1
# res [[], [1], [], [], [], [], [], []]
# i:1, j: 1, i >> j: 0, (i >> j) & 1: 0
# i:1, j: 2, i >> j: 0, (i >> j) & 1: 0
# i:2, j: 0, i >> j: 2, (i >> j) & 1: 0
# i:2, j: 1, i >> j: 1, (i >> j) & 1: 1
# --> append nums[1] = 2 at index i = 2
# res [[], [1], [2], [], [], [], [], []]
# i:2, j: 2, i >> j: 0, (i >> j) & 1: 0
# i:3, j: 0, i >> j: 3, (i >> j) & 1: 1
# --> append nums[0] = 1 at index i = 3
# res [[], [1], [2], [1], [], [], [], []]
# i:3, j: 1, i >> j: 1, (i >> j) & 1: 1
# --> append nums[1] = 2 at index i = 3
# res [[], [1], [2], [1, 2], [], [], [], []]
# i:3, j: 2, i >> j: 0, (i >> j) & 1: 0
# i:4, j: 0, i >> j: 4, (i >> j) & 1: 0
# i:4, j: 1, i >> j: 2, (i >> j) & 1: 0
# i:4, j: 2, i >> j: 1, (i >> j) & 1: 1
# --> append nums[2] = 3 at index i = 4
# res [[], [1], [2], [1, 2], [3], [], [], []]
# i:5, j: 0, i >> j: 5, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1], [], []]
# i:5, j: 1, i >> j: 2, (i >> j) & 1: 0
# i:5, j: 2, i >> j: 1, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [], []]
# i:6, j: 0, i >> j: 6, (i >> j) & 1: 0
# i:6, j: 1, i >> j: 3, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [2], []]
# i:6, j: 2, i >> j: 1, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], []]
# i:7, j: 0, i >> j: 7, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1]]
# i:7, j: 1, i >> j: 3, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2]]
# i:7, j: 2, i >> j: 1, (i >> j) & 1: 1
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]



# Bit manipulation-2:
# Beats 92.68% of users with Python3 
# Algorithm:

#Bit serial mapping
# The bit serial from 0 to 2^n - 1 can be mapped to element selection for subset generation.

# Take nums = [1,2,3] for example.

# size of input = 3.
# Thus, we go through bit serial from 0 to 2^3 -1 = ( 1 << 3 ) - 1 = 7, then getting corresponding subset on the fly.

# 0 = 0b 000 = empty set = [ ]
# 1 = 0b 001 = select first element = [ 1 ]
# 2 = 0b 010 = select second element = [ 2 ]
# 3 = 0b 011 = select first and second elements = [ 1, 2 ]
# 4 = 0b 100 = select third element = [ 3 ]
# 5 = 0b 101 = select first and third elements = [ 1, 3 ]
# 6 = 0b 110 = select second and third elements = [ 2, 3 ]
# 7 = 0b 111 = select all elements = [ 1, 2 ,3 ]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        power = 1 << n
        res = []

        # i = Subset Bit serial number
        for i in range(power):
            curr_subset = []
            for ind in range(n):
                # Add nums[ind] to curr_subset if "ind"-th bit of "i" is set to 1.
                if i & 1 << ind:   # equivalent to -> i & (1 << ind)
                    curr_subset.append(nums[ind])
            res.append(curr_subset) 
        return res

# Dry Run:
# i: 0, ind: 0, bin(i): 0b0, i & 1<<ind: 0: 
# i: 0, ind: 1, bin(i): 0b0, i & 1<<ind: 0: 
# i: 0, ind: 2, bin(i): 0b0, i & 1<<ind: 0: 
# res [[]]
# i: 1, ind: 0, bin(i): 0b1, i & 1<<ind: 1: 
# i: 1, ind = 0,nums[ind]: 1
# curr_subset [1]
# i: 1, ind: 1, bin(i): 0b1, i & 1<<ind: 0: 
# i: 1, ind: 2, bin(i): 0b1, i & 1<<ind: 0: 
# res [[], [1]]
# i: 2, ind: 0, bin(i): 0b10, i & 1<<ind: 0: 
# i: 2, ind: 1, bin(i): 0b10, i & 1<<ind: 2: 
# i: 2, ind = 1,nums[ind]: 2
# curr_subset [2]
# i: 2, ind: 2, bin(i): 0b10, i & 1<<ind: 0: 
# res [[], [1], [2]]
# i: 3, ind: 0, bin(i): 0b11, i & 1<<ind: 1: 
# i: 3, ind = 0,nums[ind]: 1
# curr_subset [1]
# i: 3, ind: 1, bin(i): 0b11, i & 1<<ind: 2: 
# i: 3, ind = 1,nums[ind]: 2
# curr_subset [1, 2]
# i: 3, ind: 2, bin(i): 0b11, i & 1<<ind: 0: 
# res [[], [1], [2], [1, 2]]
# i: 4, ind: 0, bin(i): 0b100, i & 1<<ind: 0: 
# i: 4, ind: 1, bin(i): 0b100, i & 1<<ind: 0: 
# i: 4, ind: 2, bin(i): 0b100, i & 1<<ind: 4: 
# i: 4, ind = 2,nums[ind]: 3
# curr_subset [3]
# res [[], [1], [2], [1, 2], [3]]
# i: 5, ind: 0, bin(i): 0b101, i & 1<<ind: 1: 
# i: 5, ind = 0,nums[ind]: 1
# curr_subset [1]
# i: 5, ind: 1, bin(i): 0b101, i & 1<<ind: 0: 
# i: 5, ind: 2, bin(i): 0b101, i & 1<<ind: 4: 
# i: 5, ind = 2,nums[ind]: 3
# curr_subset [1, 3]
# res [[], [1], [2], [1, 2], [3], [1, 3]]
# i: 6, ind: 0, bin(i): 0b110, i & 1<<ind: 0: 
# i: 6, ind: 1, bin(i): 0b110, i & 1<<ind: 2: 
# i: 6, ind = 1,nums[ind]: 2
# curr_subset [2]
# i: 6, ind: 2, bin(i): 0b110, i & 1<<ind: 4: 
# i: 6, ind = 2,nums[ind]: 3
# curr_subset [2, 3]
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
# i: 7, ind: 0, bin(i): 0b111, i & 1<<ind: 1: 
# i: 7, ind = 0,nums[ind]: 1
# curr_subset [1]
# i: 7, ind: 1, bin(i): 0b111, i & 1<<ind: 2: 
# i: 7, ind = 1,nums[ind]: 2
# curr_subset [1, 2]
# i: 7, ind: 2, bin(i): 0b111, i & 1<<ind: 4: 
# i: 7, ind = 2,nums[ind]: 3
# curr_subset [1, 2, 3]
# res [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
