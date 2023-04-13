'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''


from typing import List


def combinationSum2(arr: List[int], target: int) -> List[List[int]]:
    n, ind, ds, ans = len(arr),0,[],[]
    arr.sort()

    # Different pattern then pick/non-pick (here we're looping form ind -> n-1) this approach is efficient for this problem
    def helper(ind,target):
        # BASE CASE: if the target is reached, append the current solution to the answer list and return
        if target==0:
            ans.append(ds[:])  # Append a copy of the current solution (ds) to the answer list
            return

        # Iterate over the array, starting from the current index (ind)
        for i in range(ind,n):
            # No need to check further if current element is greater than remaining target
            if arr[i] > target:
                break
            # To avoid recursion skip if same element appears in next consecutive index (TO AVOID DUPLICATES)
            if i > ind and arr[i] == arr[i-1]: continue
            # Otherwise add the current element to the ds and recursively call the helper function with the remaining target
            ds.append(arr[i])
            # with i+1 not ind+1
            helper(i+1,target-arr[i])
            # Remove the current element from the solution list (ds) and continue the loop to check other possible solutions
            ds.pop()

    helper(ind,target)
    return ans


# Main code to test the function
if __name__ == "__main__":
    nums = [10,1,2,7,6,1,5]
    target = 8
    res = combinationSum2(nums,target)
    print(f"ans: {res}")
    
    
    
    
    
# Time Complexity:O(2^n*k)    
# Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will be O(2^n). 
# we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.

# Space Complexity:O(k*x)
# Reason: if we have x combinations then space will be x*k where k is the average length of the combination.
