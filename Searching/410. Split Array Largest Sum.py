# The problem is just like LC 1011
# We can use our Binary Search template for this.
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:   
        
        def feasible(threshold):  # Condition function...returns True if all subarrays sum is < threshold else False
            cnt = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:  # Total sum of current subarray is greater than threshold...so we must put this num in next subarray
                    total = num
                    cnt += 1   # Counts the number of subarrays
                    if cnt > k: return False # Number of subarrays exceeds k
            return True 
        
        left,right = max(nums),sum(nums)   # Maximum sum of any subarray will always lie between these two ranges
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):  
                right = mid   # Feasible chhe to aapne haji nani threshold value mate check kariye
            else:
                left = mid + 1
        return left


# Example:   nums = [10,7,2,12,5,11,7,13], k = 4
#            left = 13,  right = 67 
#            ans = 19      
