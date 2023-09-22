"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 
Example 4:
Input: num  = "124351", k = 3
       mins = "123311"
Output: "121"

Example 5:
Input: num  = "112", k = 1
       mins = "112"
Output: "11"

Example 7:
Input: num  = ""100"", k = 1
       mins = "0"
Output: ""
 
Constraints:
1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

# T.C :  O(N)
# S.C :  O(N)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Primary condition check
        if k >= len(num): 
            return '0'
          
        stack = []  # Maintain monotonic increasing stack

        # Pop top-most stack element if it's greater than current digit
        # Keep doing this
        # Push digit to stack at last
        for dig in num:
            while k and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)

        # If still k > 0, then remove k digits from stack top...as it's monotonous increasing stack.
        if k > 0:
            stack = stack[:-k]
            
        return ''.join(stack).lstrip('0') or '0'
