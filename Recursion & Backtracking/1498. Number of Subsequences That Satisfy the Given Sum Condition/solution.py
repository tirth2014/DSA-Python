# Brute-force approach using backtracking and finding all subsequences and filtering out those we need.  (TLE)
# Time complexity = O(2^N), where N is the number of elements in the nums list. This is because for each element, we have two choices: include it in the subsequence or not.
# Space Complexity: O(N)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt = 0
        def helper(i, arr):
          # we need to use nonlocal as "int" is "immutable". So, inside the function the outer cnt won't be identified. and new local cnt of type int will be initialized if not used nonlocal
          # Instead if it was a list then we don't need to use nonlocal kw as list is "mutable" object
          nonlocal cnt   
            if i == len(nums):
                if arr and min(arr) + max(arr) <= target:
                    cnt += 1
                return

            #pick
            arr.append(nums[i])
            helper(i+1,arr)
            arr.pop()

            #not pick
            helper(i+1,arr)

        helper(0,[])
        return cnt



# Sorting + Two-pointer  (accepted)
# Time Complexity: O(N log N)
# Space Complexity: O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans,l,r = 0,0,len(nums)-1
        mod = 10 ** 9 + 7
        while l <= r:
            if l <= r and nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += 2 ** (r - l)
                ans %= mod
                l += 1
        return and




# Most-efficient solution: beats 100% 
# Time Complexity: O(N log N)
# Space Complexity: O(N)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums, n = sorted(nums), len(nums)
        bin_arr, j = ["0"]*n, n-1
        mod = 10**9 + 7

        for i, num in enumerate(nums):
            if 2*num > target: break
            while (num + nums[j]) > target:
                j -= 1
            bin_arr[i-j-1] = "1"   # first index thi start thase as index -ve ma aavse
        
        return int("".join(bin_arr), base=2) % mod
        # For test case input: nums = [2,3,3,4,6,7], target = 12
        # "".join(binary_arr)   -->  ('111101',)
        # int("".join(bin_arr), base=2)  --> 61

        #  |  int(x, base=10) -> integer
        #  |
        #  |  Convert a number or string to an integer, or return 0 if no arguments
        #  |  are given.  If x is a number, return x.__int__().  For floating point
        #  |  numbers, this truncates towards zero.
        #  |
        #  |  If x is not a number or if base is given, then x must be a string,
        #  |  bytes, or bytearray instance representing an integer literal in the
        #  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
        #  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        #  |  Base 0 means to interpret the base from the string as an integer literal.
        #  |  >>> int('0b100', base=0)
        #  |  4
