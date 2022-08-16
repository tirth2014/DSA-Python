# Approach-1
# Traverse the array. While traversing, use the absolute value of every element as an index and make the value at this index as negative to mark it visited. If something is already marked negative then this is the repeating element. 
# T.C = O(n), S.C = O(1)

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        r,m = 0,0
        for i in range(len(A)):
            if A[abs(A[i]) -1] > 0:
                A[abs(A[i])-1] = -A[abs(A[i]) -1]
            else:
                r = abs(A[i])      # repeatedNumber
        
        for i in range(len(A)):
            if A[i] > 0:
                m = i + 1          # missingNumber
        
        return [r,m]

# Approach-2:

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        r = sum(A) - sum(set(A))
        m = n*(n+1)//2 - sum(set(A))   # note: n*(n+1)/2 is sum of first n natural numbers
        return [r,m]
      
# Approach - 3:
