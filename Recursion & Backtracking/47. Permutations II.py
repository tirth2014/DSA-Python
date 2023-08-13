"""
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

# Just a little change in Permutations I 
# Instead of using nums[i] in used condition we use "i" here.
# And to avoid duplication we use used_2 set.
# Beats 20.33%
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        used_2 = set()
        def backtrack(ds=[]):
            if len(ds) == len(nums) and tuple(ds) not in used_2:
                res.append(ds[:])
                used_2.add(tuple(ds[:]))
                return

            for i in range(len(nums)):
                if i not in used:
                    ds.append(nums[i])
                    used.add(i)
                    backtrack(ds)
                    ds.pop()
                    used.remove(i)

        backtrack()
        return res

# Optimized technique using Counter from python collections library 
# Beats 90.93% of users with Python3
"""
The time complexity of the given code for generating all unique permutations of a list of numbers is O(N * N!), where N is the length of the nums list.

1. Backtracking Steps: The backtracking algorithm explores all possible combinations of the input list, and in the worst case, it generates N! permutations. 
This is because at each level of recursion, you have N choices for the next element, then N-1 choices for the one after that (since duplicates are being accounted for), N-2 choices for the one after that, and so on, until you have only 1 choice for the last element. 
This results in a total of N * N! possible permutations.

2. Loop Over Counter: Within each backtracking call, you iterate through the counter dictionary, which contains distinct elements from the input list. 
In the worst case, this loop runs N times (for each distinct element).

The overall time complexity is therefore O(N * N!).
It's worth noting that the code might perform better than this worst-case analysis in practice, 
especially if there are many duplicate elements in the input list, as the counter dictionary helps prune some branches of the recursion 
by not exploring duplicate elements once their count has been exhausted.
"""
import ast
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ds=[], counter=Counter(nums)):
            if len(ds) == len(nums):
                res.append(ds[:])
                return

            for i in counter:
                print('i: %s, counter: %s' % (i, counter))
                if counter[i] > 0:
                    ds.append(i)
                    print('ds', ds)
                    counter[i] -= 1
                    backtrack(ds, counter)
                    popped = ds.pop()
                    print('popped: %s, ds: %s' % (popped, ds))
                    counter[i] += 1

        backtrack()
        return res


if __name__ == '__main__':
    ob = Solution()
    i1 = input("enter nums list: ")
    i1 = ast.literal_eval(i1)
    print("i1: ", i1)
    ans = ob.permuteUnique(i1)
    print('result:', ans)


# For understanding the second approach:
'''
enter nums list: [1,1,2]
i1:  [1, 1, 2]
i: 1, counter: Counter({1: 2, 2: 1})
ds [1]
i: 1, counter: Counter({1: 1, 2: 1})
ds [1, 1]
i: 1, counter: Counter({2: 1, 1: 0})
i: 2, counter: Counter({2: 1, 1: 0})
ds [1, 1, 2]
popped: 2, ds: [1, 1]
popped: 1, ds: [1]
i: 2, counter: Counter({1: 1, 2: 1})
ds [1, 2]
i: 1, counter: Counter({1: 1, 2: 0})
ds [1, 2, 1]
popped: 1, ds: [1, 2]
i: 2, counter: Counter({1: 1, 2: 0})
popped: 2, ds: [1]
popped: 1, ds: []
i: 2, counter: Counter({1: 2, 2: 1})
ds [2]
i: 1, counter: Counter({1: 2, 2: 0})
ds [2, 1]
i: 1, counter: Counter({1: 1, 2: 0})
ds [2, 1, 1]
popped: 1, ds: [2, 1]
i: 2, counter: Counter({1: 1, 2: 0})
popped: 1, ds: [2]
i: 2, counter: Counter({1: 2, 2: 0})
popped: 2, ds: []
result: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
'''
