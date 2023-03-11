# Recursive - 1 (My solution)

class Solution:

    def binarySearch(self,arr,target,l,r):
        mid = (l+r)//2
        
        if arr[mid] == target:
            return mid
        elif target > arr[mid] and r != 0 and l != r and not (mid == len(arr)-1 and target>arr[mid]) and r!=mid:
            return self.binarySearch(arr, target, mid + 1, r)
        elif target < arr[mid] and r != 0 and l != r and not (mid == 0 and target<arr[mid]) and l!=mid:
            return self.binarySearch(arr, target, l, mid - 1)
        else:
            return mid+1 if target > arr[mid] else mid

    def searchInsert(self, nums: List[int], target: int) -> int:
        
        ind = self.binarySearch(nums,target,0,len(nums)-1)
        return ind
      
#  Recursive - 2
#  There wasn't any need to expand conditions...jst if left <= right single condition is enough.

class Solution:

    def binarySearch(self,arr,target,l,r):
        while l<=r:
            mid = (l+r)//2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                return self.binarySearch(arr, target, mid + 1, r)
            else:
                return self.binarySearch(arr, target, l, mid - 1)
        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        
        ind = self.binarySearch(nums,target,0,len(nums)-1)
        return ind
      
# Iterative  

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return l

# Using python bisect library:

from bisect import bisect
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums,target)
