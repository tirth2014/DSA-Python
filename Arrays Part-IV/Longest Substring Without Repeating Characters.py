class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        max_cnt = 0
        for r in range(len(s)):
            if s[r] not in seen:
                max_cnt = max(max_cnt,r-l+1)
            else:       # s[r] in seen
                # case-1: s[r] is outside the current window, we can keep expanding the current window by moving rigth ptr
                # case-2: s[r] inside current window, we need to change the current window by moving the left ptr to seen[s[r]]+1
                if seen[s[r]] < l:
                    max_cnt = max(max_cnt,r-l+1)        
                else:
                    l = seen[s[r]]+1
            seen[s[r]] = r
        return max_cnt
      
# T.C => O(N)
# S.C => O(M)
