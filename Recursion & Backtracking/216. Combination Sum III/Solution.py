# Beats 8.44%
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(i=1,arr=[]):
            if len(arr) == k or i > 9:
                if sum(arr) == n and len(arr) == k:
                    ans.append(arr[:])
                return

            #pick
            arr.append(i)
            helper(i+1)
            arr.pop()

            #not pick
            helper(i+1)

        helper()
        return ans


# Slightly optimized:
# Beats 79.64%
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(i=1,arr=[],curr_sum=0):
            if len(arr) == k:
                if sum(arr) == n:
                    ans.append(arr[:])
                return

            if i > 9 or curr_sum > n:
                return

            #pick
            arr.append(i)
            helper(i+1, arr, curr_sum+i)
            arr.pop()

            #not pick
            helper(i+1, arr, curr_sum)

        helper()
        return ans


from itertools import combinations

# Python library solution. Create all k-combinations of digits and keep those with sum n:
class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
