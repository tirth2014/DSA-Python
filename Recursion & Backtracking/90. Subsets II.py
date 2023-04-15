'''
Given an integer array nums that may contain duplicates, return all possible subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''

# Approach-1 : Pick & Not pick
class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i,n,ds,ans = 0,len(arr),[],[]

        def helper(i,ds,ans):
            if i == n:
                if ds not in ans:
                    ans.append(ds[:])
                return

            # Pick
            ds.append(arr[i])
            helper(i+1,ds,ans)
            ds.pop()

            # Not pick
            helper(i + 1, ds, ans)

        helper(i,ds,ans)
        return ans
       
# The time complexity of this code is O(2^n * n), where n is the length of the input array arr.
# In each recursive call, we have two choices - either we pick the current element or we don't pick it. 
# So, the number of recursive calls will be 2^n. For each subset, we also make a copy of the current subset using ds[:], which takes O(n) time. 

# The space complexity of this code is O(n^2). This is because we are using a list ds to store the current subset, which can have at most n elements. 
# In addition, for each subset, we are making a copy of the current subset using ds[:], which also takes O(n) space. Therefore, the overall space complexity is O(n^2).
# Note that the use of "if ds not in ans" also contributes to the time complexity of the code, as it requires iterating over all the elements of ans to check for duplicates.        
      
      
      
      
# Approach-2: Using for loop from ind -> n-1 in recursion
class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ind,n,ds,ans = 0,len(arr),[],[]
    
        # Backtrack method
        def findSubsets(ind):
            ans.append(ds[:])

            for i in range(ind,n):
                # To avoid duplicates
                # If the element being added is same as previous (i.e. consecutively repeated) then don't avoid recursion
                # EXCEPTION: if the element is appearing for first time(i == ind) then continue the flow doesn't matter if it's previous element is same
                if i != ind and arr[i] == arr[i-1]:
                    continue
                ds.append(arr[i])
                findSubsets(i+1)
                ds.pop()

        findSubsets(ind)
        return ans
       
# Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).
# Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.         



       
# Approach-3: Iterative (with Hashing)

# The idea is that we start with an empty subset.
# For each element num in nums, we iterate all all previous subsets, create new subsets by adding each previous subsets with num.
# For example: nums = [1, 2, 3]
# First at all, ans = [[]]
# Step 1, with nums[0] = 1, ans = [[], [1]]
# Step 2, with nums[1] = 2, ans = [[], [1], [2], [1, 2]]
# Step 3, with nums[2] = 3, ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        ans.add(tuple())

        for num in nums:
            new_subsets = set()
            for subset in ans:
                new_subsets.add(tuple(list(subset) + [num]))
            ans.update(new_subsets)
        return ans
       
# Complexity

# Time: O(2^N * N), where N <= 10 is length of nums array.
# Space: O(2^N)       

                   
