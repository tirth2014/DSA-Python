"""
139. Word Break
https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Example 4:
Input: s = "cars", wordDict = ["car","ca","rs"]
Output: false

Example 5:
Input: 
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaa......]
output: false
"""

# Approach-1: (Fails for some cases like Example 4)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if word in s:
                s = s.replace(word,'')
        return True if s == '' else False


# Approach-2: Only pure recursion
# Inefficient approach ( TLE for cases like Example 5)
# For each character 'a' in the string, the algorithm will try different word combinations from the word dictionary, 
# leading to a large number of redundant calculations. As a result, the algorithm's execution time will grow rapidly with the length of the string and the size of the word dictionary.
# leading to exponential time complexity.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        for word in wordDict:
            if s.startswith(word) and self.wordBreak(s[len(word):], wordDict):
                return True
        return False
