
import ast
from typing import List
import heapq

# Space O(N)
# Time O(N)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        # Using prefix sum algorithm
        # This approach works for array with all elements either +ve, -ve etc...
        # at every index if prefix sum is 's', we're looking for
        # no. of subarrays before that element with prefix_sum 's-k'
        # storing 0 in dict/hashmap(pref_sum: cnt) is very important
        # s = prefix sum
        # k = goal
        # dict = prefix sum count dictionary
        dict = {}
        s, res = 0, 0
        dict[0] = 1
        for num in nums:
            s += num
            res += dict.get(s - k, 0)
            dict[s] = dict.get(s, 0) + 1
        return res
      

if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        # arr = list(map(int, input("arr: ").split()))
        arr = ast.literal_eval(input("arr: "))
        # st = input("string: ")
        # num = input("num string: ")
        k = int(input("goal: "))
        ans = ob.numSubarraysWithSum(arr, k)
        print(ans)
