# Brute Force - O(N^2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1==n2:
                    res.add(n1)
        return res
      

# Sorting + Two Pointer -  O(NlogN)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j=0,0
        res = set()
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
        return res
      
      
# Using HashMap(dictionary)  -  O(N)
# Dictionary lookup is O(1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = set()
        
        for n1 in nums1:
            if n1 not in seen:
                seen[n1] = 1
            else:
                continue
        
        for n2 in nums2:
            if n2 in seen:
                res.add(n2)
            else:
                continue
        
        return res
      

# One-liner using set intersection - Most optimized:
#  O(min(len(nums1), len(nums2))
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
      
        # We can use '&' also for intersection of sets
        # return set(nums1) & set(nums2)
              
