# HashMap Approach
# The time complexity is O(n), where n is the length of the input list nums. This is because the function iterates through nums twice, which takes O(n) time, and the dictionary freq operations such as get() and in checks take O(1) time on average.
# The space complexity is O(n), as the dictionary freq can store up to n elements in the worst case scenario where all the elements in nums are unique.
class Solution:
    def findLHS(self, nums):
        freq,ans = {},0
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num in freq:
            if num+1 in freq:
                ans = max(ans,freq[num]+freq[num+1])
        return ans
      
      
# Python 2 liner - Same using collections.Counter:
class Solution:
    def findLHS(self, nums):
        C = Counter(nums)
        return max((C[n] + C[n+1])*(C[n+1] != 0) for n in C)
        # True = 1 and False = 0 that's why multiplied by (C[n+1] != 0)
      
