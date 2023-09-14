"""
204. Count Primes
https://leetcode.com/problems/count-primes/description/

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 10^6
"""

# Naive (Gives TLE):
class Solution:
    def isPrime(self,n: int) -> bool:
        if n in [0,1]: return False
        sqrt_n = int(n ** (1/2))  # or int(math.sqrt(n))
        for i in range(2, sqrt_n+1):
            if i != n and n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        cnt = 0
        for num in range(n):
            if self.isPrime(num): cnt += 1
        return cnt
      

# Optimal Solution - using Sieve of Eratosthenes
class Solution:
    def countPrimes(self, N: int) -> int:
        if N in [0,1]: return 0
        sieve = [1] * N
        sieve[0] = sieve[1] = 0
        for i in range(2, int(N**0.5)+1):
            if sieve[i]:
                sieve[i*i:N:i] = [0] * ((N-1-i*i)//i + 1)
              
                # slower
                # for j in range(i*i, N, i):
                #     sieve[j] = 0
      
                # almost 3x faster
                # sieve[i*i:N:i] = [0] * ((N-1-i*i)//i + 1)
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s[10] = 0, 0, 0, 0
        return sum(sieve)
