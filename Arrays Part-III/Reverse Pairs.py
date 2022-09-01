# Using Enhanced MergeSort - O(NlogN) time and O(N) space

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

# Using BinaryIndexTree (Fenwick Tree): O(NlogN) time complexity & O(N) space   

class Solution:
    class BIT:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (self.n + 1)

        def update(self, i, x):
            while i <= self.n:
                self.bit[i] += x  # (i&-i,i) gives the first rightmost SET bit of the number in binary
                i += i & -i

        def sum(self, i):
            ans = 0
            while i > 0:
                ans += self.bit[i]
                i -= i & -i
            return ans

    def reversePairs(self,nums):
        nnums = list(set(nums + [2*x for x in nums]))  # Note:  list1 + list2 = Appended list (NOT Sum of elements from both list)
        print("new nums: ", nnums)
        nnums.sort()
        print("sorted nn: ", nnums)
        tree = self.BIT(len(nnums))
        print("BIT is: ",tree.bit)
        res = 0
        ranks = {}
        for i, n in enumerate(nnums):
            ranks[n] = i + 1
        print("Ranks: ",ranks)
        for n in nums[::-1]:
            res += tree.sum(ranks[n] - 1)
            tree.update(ranks[n * 2], 1)
        return res
                    
                                    
                
