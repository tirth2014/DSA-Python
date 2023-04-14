'''
Given a list arr of N integers, print sums of all subsets in it.

Example 1:

Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.


Example 2:

Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8

Expected Time Complexity: O(2^N)
Expected Auxiliary Space: O(2^N)

Constraints:
1 <= N <= 15
0 <= arr[i] <= 10^4

'''


class Solution:
	def subsetSums(self, arr, n):
	    i,ds,ans = 0, [],[]

        def helper(i,ds,ans):
            # BASE CASE
            if i == n:
                ans.append(sum(ds))
                return

            # Pick
            ds.append(arr[i])
            helper(i+1,ds,ans)
            ds.pop()

            # Non pick
            helper(i+1,ds,ans)
        helper(i,ds,ans)
        return ans
