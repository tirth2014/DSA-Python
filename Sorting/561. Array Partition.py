# O(NlogN) and O(1)
# No need to find pairs,combinations any such stuff...it's jst a basic problem
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        # jump 2 elements in each iteration
        for i in range(0,len(nums),2):
            max_sum += nums[i]
        return max_sum
      
# 2 Liner:
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0,len(nums),2)])
      
      
# 1 Liner very pythonic 
# The space complexity is O(n) because a new list is created containing every second element of the sorted list.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
    
    
# Optimized solution using Counting Sor:
# When to use Counting Sort:
# Counting sort is an efficient sorting algorithm when the range of input values is small. which is here 10^4 only.

# Time Complexity = O(N+k) = O(N+20002) = O(N)
# Space Complexity = O(k) = O(20002) = O(1)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Here,arr is an auxiliary array used as a frequency table to hold the count of each value in the input list.
        # The reason the length of arr is chosen to be 20002 is because the input values are in the range [-10000, 10000].
        # Therefore, to accommodate negative numbers, the index of arr for each element in nums is el + 10000, 
        # which shifts the range of indices from [-10000, 10000] to [0, 20000]. The length of arr is set to 20002 to accommodate the extra indices at both ends.
        arr = [0]*20002
        
        # Here we are doing +10000 to prevent array outbound as larger negative values can cause index error. 
        # For example, if the minimum value in nums is -10000, then without adding 10000 to the index, arr[-10000] will be out of range and cause an IndexError.
        # Adding 10000 to the index ensures that the index range is from 0 to 20001, which can accommodate all possible values in nums.
        # Here We're adding frequency count of each element in arr at index = element
        for el in nums: arr[el+10000] += 1

        curr,max_sum = 0,0
        for i in range(len(arr)):
            while arr[i] != 0:
                # adds the current element to the result max_sum if curr is even, which means we have just started a new pair.
                # odd curr means aapni pase already curr pair ni minimum value chhe. 
                if curr%2 == 0: max_sum += i-10000
                curr+=1
                arr[i]-=1
        return max_sum
            



            
        

        
      
      
