# Brute Force
# O(N^2)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] == 2*arr[i] or arr[i] == 2*arr[j]:
                    return True
        return False
     
# Time complexity:
# sort - O(nlogn)
# binary search for each element in worst case - O(nlogn)
# overall - O(nlogn)
# Space complexity:
# O(1)    

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            element.
            if arr[i]>=0:
                # Binary seach the whole array right to the current 
                l,r = i+1,len(arr)-1
            else:
                # We have to handle the case of negative numbers in array also.
                # We binary search the array left to current element i if i < 0
                l,r = 0,i-1
            while l<=r:
                target = 2*arr[i]
                m=l+(r-l)//2
                if arr[m] == target:
                    return True
                elif target > arr[m]:
                    l=m+1
                else:
                    r=m-1
        return False    
