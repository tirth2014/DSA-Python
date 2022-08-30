# Using Enhanced MergeSort

class Solution:
    def reversePairs(self, arr):
        count = 0
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            
            count += self.reversePairs(L)
            count += self.reversePairs(R)
            
            # Ye hai Main Logic - O(N) kyuki j ko hum jaha hai wahi se aage badha rahe...na ki har baar starting se start kar rhe 
            j = 0
            for i in range(len(L)):
                while j < len(R) and L[i] > 2*R[j]:
                    j+=1
                count += j

            # Merge    
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    # for r in range(i, len(L)):
                    #     if L[r] > 2 * R[j]:
                    #         self.count += 1
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return count
      
# T.C : O(NlogN) + O(N) + O(N)          

# Using BinaryIndexTree (Fenwick Tree): (To be Solved)            
                    
                
