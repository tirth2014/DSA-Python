'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
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
