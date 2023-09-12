# Optimal - bit manipulation approach:
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
