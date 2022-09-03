# Using Binary Search - O(N + NlogN) time and O(N) space

class Solution:
    def binarySearch(self,arr, item, cur):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > item:  # item is on left side
                r = mid - 1
            elif arr[mid] < item:
                l = mid + 1
            elif arr[mid] == item and (arr.count(item) > 1 or arr[mid] != cur):
                return mid
            else:
                return None

    def twoSum(self, nums, target):
        nn = sorted(nums)
        d = {}
        for i,n in enumerate(nums):
            d[n] = i
        for i in range(len(nums)):
            ind = self.binarySearch(nn,target-nums[i], nums[i])
            if ind is not None or ind == 0:
                j = d.get(nn[ind])
                return [i,j] 
              
# Using Only Dictionary - O(N) time and O(N) space
class Solution:   
    def twoSum(self, nums, target):
        d = {}
        for i,n in enumerate(nums):
            dif = target - nums[i]
            if dif in d:
                return [d[dif], i]
            else:
                d[n] = i
                
# Using Two Pointer Approach:  O(N + NlogN) time and O(N) space
class Solution:
    def twoSum(self, nums, target):
        arr = []
        for i, n in enumerate(nums):
            arr.append([n, i])
        arr.sort()
        l, r = 0, len(arr) - 1
        while l < r:
            temp_sum = arr[l][0] + arr[r][0]
            if temp_sum == target:
                return [arr[l][1], arr[r][1]]
            elif target > temp_sum:
                l += 1
            elif target < temp_sum:
                r -= 1
              
        
