# Brute Force
# Time Complexity = O(n^2)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s or s.count(char) < t.count(char):
                return char
              
              
# Time Complexity = O(nlogn)              
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        i=j=0
        # one-one pointer for s and t list each.
        while i<len(s) and j<len(t):
            if s[i] != t[j]:
                return t[j]
            i+=1
            j+=1
        return t[j]              
              
              
# Time Complexity = O(n)
# Space Complexity = O(n)        
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = {i:0 for i in t}
        for ch in t:
            cnt[ch] += 1

        for ch in s:
            cnt[ch] -= 1

        for key in cnt:
            if cnt[key] == 1:
                return key
              
              
# Using bitwise XOR:
"""
s = abc
t = cabx

if we take XOR of every character. all the n character of s "abc" are similar to n character of t "cab". So, they will cancel each other. 
And we are left with our answer.

s =   abc
t =   cbax
------------
ans -> x
-----------
Time Complexity :- O(N)
Space Complexity :-O(1)
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for cs in s: c ^= ord(cs)  # ord gives equivalent ascii code of char
        for ct in t: c ^= ord(ct)

        return chr(c)   # ascii to char
        
        
# One liner XOR solution same as above:

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda x,y: x^y, map(ord,s+t)))
        
