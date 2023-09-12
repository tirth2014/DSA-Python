"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1].
For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.


Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Example 3:
Input: dividend = -2147483648, divisor = 1
Output: -2147483648

Example 4:
Input: dividend = 2147483648, divisor = 1
Output: 2147483647


Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""

# Approach-1:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        is_positive = ((dividend > 0) == (divisor > 0))  # If both have same sign, ans is +ve
        ans, dd, dv = 0, abs(dividend), abs(divisor)
        while dd >= dv:  # while dividend is greater than or equal to divisor
            temp, i = dv, 1
            while dd >= temp:
                dd -= temp
                ans += i
                i <<= 1
                temp <<= 1
        if ans == (1 << 31) and is_positive:
            return (1 << 31)-1
        return ans if is_positive else -ans



#Approach-2: bit manipulation approach:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        is_positive = ((dividend > 0) == (divisor > 0))  # If both have same sign, ans is +ve
        ans, dd, dv = 0, abs(dividend), abs(divisor)
        while dd >= dv:  # while dividend is greater than or equal to divisor
            q = 0
            while dd > (dv << q+1):
                q += 1
            ans += 1 << q    # add the power of 2 found to the answer
            dd -= (dv << q)  # reduce the dividend by divisor * power of 2 found
        if ans == (1 << 31) and is_positive:  # if ans cannot be stored in signed int
            return (1 << 31) - 1
        return ans if is_positive else -ans


if __name__ == '__main__':
    ob = Solution()
    dividend = int(input("dividend: "))
    divisor = int(input("divisor: "))
    ans = ob.divide(dividend,divisor)
    print("ans: ",ans)
