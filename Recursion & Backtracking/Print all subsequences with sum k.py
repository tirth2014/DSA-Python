class Solution:
    def subsequences_sum_k(self,i,arr,k,n,ds=[],sum=0):
        # BASE CASE
        if i == n:
            if sum == k:
                print(ds)
            return
          
        # PICK CASE
        ds.append(arr[i])
        sum += arr[i]
        self.subsequences_sum_k(i+1,arr,k,n,ds,sum)
        ds.pop()
        sum -= arr[i]

        # NOT PICK CASE
        self.subsequences_sum_k(i+1,arr,k,n,ds,sum)

ob = Solution()
arr = [1,3,2,2,5,2,3,7]
k=7
ob.subsequences_sum_k(0,arr,k,len(arr))

# OUTPUT:
# [1, 3, 3]
# [1, 2, 2, 2]
# [3, 2, 2]
# [3, 2, 2]
# [3, 2, 2]
# [2, 2, 3]
# [2, 5]
# [2, 2, 3]
# [2, 5]
# [2, 2, 3]
# [5, 2]
# [7]
