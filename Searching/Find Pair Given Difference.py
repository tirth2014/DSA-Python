"""
Method 2: We can use sorting and Binary Search to improve time complexity to O(nLogn). 
The first step is to sort the array in ascending order. Once the array is sorted, 
traverse the array from left to right, and for each element arr[i], binary search for arr[i] + n in arr[i+1..n-1].
If the element is found, return the pair. Both first and second steps take O(nLogn).
So overall complexity is O(nLogn). 
"""
class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        for i in range(L):
            target = arr[i] + N
            l,r = i+1,L-1
            while l<=r:
                m = l+(r-l)//2
                if arr[m] == target:
                    return True
                elif target > arr[m]:
                    l = m+1
                else:
                    r = m-1
        return False
                

"""
Method 3: The second step of the Method -2 can be improved to O(n). The first step remains the same(sorting). 
The idea for the second step is to take two index variables i and j, and initialize them as 0 and 1 respectively. 
Now run a linear loop. If arr[j] – arr[i] is smaller than n, we need to look for greater arr[j], so increment j. 
If arr[j] – arr[i] is greater than n, we need to look for greater arr[i], so increment i. 
"""
class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        i,j = 0,1
        while i < L and j < L:
            diff = arr[j] - arr[i]
            if i != j and diff == N:
                return True
            elif diff > N:
                i += 1
            else:
                j += 1
        return False
