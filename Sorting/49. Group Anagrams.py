"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

# O(n*klogk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for s in strs:
            sortedstr = ''.join(sorted(s))
            if sortedstr in dt:
                dt[sortedstr].append(s)
            else:
                dt[sortedstr] = [s]
        return list(dt.values())
      
        
# O(n*klogk)        
from collections import defaultdict
# The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. 
# It provides a default value for the key that does not exists.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        for s in strs:
            sortedstr = ''.join(sorted(s))
            dt[sortedstr].append(s)
        return list(dt.values())
        
        
                
# This approach considers the frequency of characters in a string to group anagrams.
# O(n*k) where n is the length of the input list strs and k is the maximum length of a string in strs. 
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dt[tuple(count)].append(s)
        return list(dt.values())          
        
