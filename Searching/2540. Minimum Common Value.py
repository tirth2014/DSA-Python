# Brute Force 
# TLE  :-P
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)

        if n1<n2:
            for i in nums1:
                if i in nums2:
                    return i
                else:
                    continue
        else:
            for i in nums2:
                if i in nums1:
                    return i
                else:
                    continue
        return -1
      
# Using Sets:
# T.C. = O(min(len(nums1),len(nums2)))
# S.C = O(min(n,m))
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        commons = set(nums1) & set(nums2)
        return min(commons) if commons else -1 
      
# Using HashMap (Dictionary)
# T.C. = O(n+m)
# S.C. = O(n)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        cnt_dic = {}

        for num in nums1:
            if num not in cnt_dic:
                cnt_dic[num] = 1
            else:
                cnt_dic[num] += 1
        
        for num in nums2:
            if num in cnt_dic:
                return num

        return -1
      
# Using Binary Search
# T.C. = O(n*logm)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        for num in nums1:             # Need to iterate over this loop too.
            l,r = 0, len(nums2)-1
            while l <= r:
                m = (l+r)//2
                if nums2[m] == num:
                    return num
                elif nums2[m] > num:
                    r = m -1
                else:
                    l = m+1
        return -1      
        
        
# Using a Two pointer approach  [BEST]
# T.C. = O(n+m)
# S.C. = O(1)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n1,n2 = len(nums1),len(nums2)
        
        while i <= n1-1 and j <= n2-1:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
        return -1

 
