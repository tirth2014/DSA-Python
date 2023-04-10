class Solution:
    def one_subsequences_sum_k(self,i,arr,k,n,ds=[],sum=0):
        # CONDITION [TO STOP RECURSION IF CERTAIN CONDITION IS MET] + BASE CASE
        if i == n:
            if sum == k:
                print(ds)
                return True
            return False
        # PICK CASE
        ds.append(arr[i])
        sum += arr[i]
        # NO FURTHER RECURSIVE CALLS NEEDED IF CONDITION IS SATISFIED
        if self.one_subsequences_sum_k(i+1,arr,k,n,ds,sum): return True
        ds.pop()
        sum -= arr[i]

        # NOT PICK CASE
        # NO FURTHER RECURSIVE CALLS NEEDED IF CONDITION IS SATISFIED
        if self.one_subsequences_sum_k(i+1,arr,k,n,ds,sum): return True

ob = Solution()
arr = [1,3,2,2,5,2,3,7]
k=7
ob.one_subsequences_sum_k(0,arr,k,len(arr))
