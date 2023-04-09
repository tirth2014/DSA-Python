# My two-pointer approach:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t == "": return True
        i = j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if j == len(t) and i <= len(s)-1: 
            return False
        else:
            return True        
          
# Efficient two-pointer approach:
# The time complexity is O(m+n), where m and n are the lengths of s and t respectively.
# This is because we are iterating through both strings using two pointers.
# In the worst case, we will need to iterate through the entire string t to check if s is a subsequence of t.
# The time complexity is not affected by the values of the strings.

# The space complexity is O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
      
      
      
# RECURSIVE APPROACH:
# The time complexity of this recursive solution is O(n), where n is the length of t.
# In the worst case, where s is not a subsequence of t, we will need to iterate through the entire string t to find out.
# The time complexity is not affected by the length or the content of the s string.

# The space complexity is O(n), where n is the length of t.
# This is because the recursive calls to self.isSubsequence are added to the call stack, and the space used by the call stack is proportional to the number of recursive calls.
# In the worst case, where the s and t strings are the same length, we will have n recursive calls, resulting in O(n) space complexity.
# However, in the best case, where s is an empty string, we will only have one recursive call, resulting in O(1) space complexity.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:],t[1:]) # Move both strings pointers to 1 postion forward
        else:
            return self.isSubsequence(s,t[1:]) # Move only t string's pointer to 1 postion forward
