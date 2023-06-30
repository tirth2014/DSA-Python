# Problem - combinations
# Decision space- numbers from 1 to n without repetition
# Output- all combinations of numbers from 1 to n of size k

#1 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(remain,arr,nxt):
            # solution found
            if remain == 0:
                ans.append(arr[:])
            else:
                # iterate through all candidates
                for i in range(nxt,n+1):
                    # add candidate
                    arr.append(i)
                    # backtrack
                    backtrack(remain-1,arr,i+1)
                    # remove candidate
                    arr.pop()
        backtrack(k,[],1)
        return ans

#2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            temp = []
            for c in combs:
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
            combs = temp
        return combs

#3 (fastest)
from itertools import combinations 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1),k))
