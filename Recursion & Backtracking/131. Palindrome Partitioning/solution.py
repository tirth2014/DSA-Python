# My solution (WRONG)
# For s = "aabb" it only returns [[a,a,b,b]]
from typing import List
class Solution:

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(p_ind=0,p_ind_last=0,arr=[],s1=s):
            if p_ind >= len(s1):
                ans.append(arr[:])
                return
            l_substr = s1[:p_ind+1]
            r_substr = s1[p_ind+1:]
            if self.isPalindrome(l_substr):
                arr.append(l_substr)
                dfs(p_ind,p_ind_last+1,arr,r_substr)
                p_ind+=1
            else:
                return
        dfs()
        return ans

if _name_ == '__main__':
    ob = Solution()
    i1 = str(input("enter string: "))
    print(i1)
    ans = ob.partition(i1)
    print(ans)


# AC backtracking solution:
# Beats 57.61% of users with Python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(ind=0):
            n = len(s)
            if ind == n:
                ans.append(path[:])
                return
            for i in range(ind,n):
                l_substr = s[ind : i+1]
                if isPalindrome(l_substr):
                    path.append(l_substr)
                    dfs(i+1)
                    path.pop()

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        dfs()
        return ans
