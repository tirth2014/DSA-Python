# My merge sort approach 
# bau kharab time complexity aave chhe - beats only 6% and memory beats only 16%

class Solution:
    def merge(self, arr, L, R):
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


    def mergeSort(self, arr, n):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L,n)
            self.mergeSort(R,n)
            self.merge(arr, L, R)

            if len(arr) == n:
                return arr

    def thirdMax(self,nums):
        if len(nums) == 1:
            return nums[0]
        nums = self.mergeSort(nums, len(nums))  # sorted nums
        seen = set()
        seen = [x for x in nums if not (x in seen or seen.add(x))]
        third_max = seen[-3] if len(seen) >= 3 else False
        first_max = seen[-1] if seen else False
        return third_max if (third_max or str(third_max)=='0') else first_max
      
      
# Follow up: Can you find an O(n) solution?
      
