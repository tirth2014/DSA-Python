class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # sum of lengths of all contiguous substrings (sum of all window's).
        res = (n*(n+1))//2

        # subtract all substrings containing only from [a,b,c,ab,bc,ac] to get no. of strings with atleast one a,b and c
        abc_cnt = {'a': 0, 'b': 0, 'c': 0}
        i, j = 0, 0
        while j < n:
            abc_cnt[s[j]] += 1
            while i < j and abc_cnt['a'] > 0 and abc_cnt['b'] > 0 and abc_cnt['c'] > 0:
                abc_cnt[s[i]] -= 1
                i += 1
            res -= (j-i+1)
            j += 1
        return res




# Time complexity: O(n)
# Space complexity: O(27) for dictionary
# By using sliding window, when we get the first window containing a,b,c, 
# then the no. of valid substrs. will be = 1 + (remaining chars. outside this window)
# For ex. s = aabcbbc...here first window with a,b,c is [aabc] so for this window #valid substrs = 4
# Likewise we can go on for every window and sum them to get result.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i = j = res = 0
        abc_cnt = {'a': 0, 'b': 0, 'c': 0}
        while j < n:
            abc_cnt[s[j]] += 1
            while abc_cnt['a'] > 0 and abc_cnt['b'] > 0 and abc_cnt['c'] > 0:
                res += (n-j)
                abc_cnt[s[i]] -= 1
                i += 1
            j += 1
        return res  
