'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

# Why list is used here as an input instead of string? => because, In Python, strings are immutable, which means their contents cannot be
# modified once they are created. Therefore, any operation that appears to modify a string actually creates a new string object with the
# desired modifications.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]
            
            

# s[:] returns a new list object that has the same elements as the original list. This new list is a separate object in memory, 
# but the elements themselves are still references to the original objects.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1] # in-place
        # s = s[::-1]  # Not in-place

                    

        
