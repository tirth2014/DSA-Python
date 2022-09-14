# O(NlogN) time,  O(N) space
class Solution:
    def maxLen(self,n, arr):
        curr_sum = 0
        prefix_sum = {}
        ans = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == 0:
                ans = i+1
            elif curr_sum in prefix_sum:
                ans = max(ans,i-prefix_sum[curr_sum])
            else:
                prefix_sum[curr_sum] = i
        return ans

 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Driver Code Ends
