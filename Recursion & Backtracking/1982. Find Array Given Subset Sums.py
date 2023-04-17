'''
1982. Find Array Given Subset Sums

You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).

Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at least one correct answer.


Example 1:

Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
Output: [1,2,-3]
Explanation: [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.

Example 2:

Input: n = 2, sums = [0,0,0,0]
Output: [0,0]
Explanation: The only correct answer is [0,0].

Example 3:

Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
Output: [0,-1,4,5]
Explanation: [0,-1,4,5] is able to achieve the given subset sums.


Example 4:
Input: n = 3, sums = [0,1,2,3,5,6,7,8]
Output: [1,2,5]


Constraints:

1 <= n <= 15
sums.length == 2n
-104 <= sums[i] <= 104
'''

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        res = []  # Result set

        while len(sums) > 1:
            num = sums[-1] - sums[-2]  # max - secondMax
            excluding = []  # Subset sums that do NOT contain num
            including = []  # Subset sums that contain num
            counterMap = collections.Counter(sums)  # Get frequency count of each element in sums

            for x in sums:
                if counterMap.get(x) > 0:
                    excluding.append(x)
                    including.append(x+num)
                    counterMap[x] -= 1
                    counterMap[x+num] -= 1
            
            # Check validity of excluding set
            if 0 in excluding:  # means the element num in original array res is positive
                sums = excluding
                res.append(num)
            else:               # means the element num in original array res is negative
                sums = including
                res.append(-1*num)
        
        return res
      
      
      
# Recursive solution (same as above):
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def helper(sums):
            # Base Case
            if len(sums) == 1:
                return []
            
            sums.sort()
            num = sums[-1] - sums[-2]  # max - secondMax
            excluding = []  # Subset sums that do NOT contain num
            including = []  # Subset sums that contain num
            counterMap = collections.Counter(sums)  # Get frequency count of each element in sums

            for x in sums:
                if counterMap.get(x) > 0:
                    excluding.append(x)
                    including.append(x+num)
                    counterMap[x] -= 1
                    counterMap[x+num] -= 1
            
            # Check validity of excluding set
            if 0 in excluding:  # means the element num in original array res is positive
                res = [num] + helper(excluding)
            else:               # means the element num in original array res is negative
                res = [-1*num] + helper(including)
            
            return res
        
        return helper(sums)
      
# In this implementation, the helper function is a recursive function that takes a list of subset sums as input and returns the corresponding array of integers. 
# It works in the same way as the original function, but instead of modifying the input list sums, it calls itself with the appropriate subset of sums and 
# constructs the output array by concatenating the result of the recursive call with the appropriate integer. 
# The base case is when the input list contains only one element, in which case it returns a list containing just that element.

# Note that this implementation has the same time complexity as the original function, but may use more memory due to the recursive calls.
            
        
      

                    
            
        
