"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""

# Solution-1:
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            if n % 2:
                ans += 1
            n = n >> 1
        return and



# Solution-2:
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1 # add 1 if n is odd
            n = n >> 1   # right-shift n by 1 position (same as n//2 but faster)
        return cnt



# Solution-3:
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n-1)   # n & n-1 removes rightmost 1-bit from n. Ex: n=6(110) then n-1 = 5(101). so, 110 & 101 = 100
            cnt += 1
        return cnt

if __name__ == '__main__':
    ob = Solution()
    num = int(input("N: "))
    print(f"{num}: {bin(num).replace('0b','')}")
    ans = ob.hammingWeight(num)
    print('#of 1 bits: ',and)
