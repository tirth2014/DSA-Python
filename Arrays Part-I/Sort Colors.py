class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k = 0,0,len(arr)-1

        while j<=k:
            if arr[j] == 0:
                arr[j],arr[i] = arr[i], arr[j]
                i+=1
                j+=1
            elif arr[j] == 2:
                arr[j],arr[k] = arr[k], arr[j]
                k-=1
            else:
                j+=1
