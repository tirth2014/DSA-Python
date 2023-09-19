# Only works for array with distinct (unique) elements
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> List[int]:
        subarrays = []

        def dfs(curr, i):
            if i == len(arr):
                subarrays.append(curr[:])
                return

            # pick
            if not curr or curr[-1] == arr[i-1]:  # this condition prevents non-contiguous distinct elements from being added.
                curr.append(arr[i])
                dfs(curr, i+1)
                curr.pop()

            # not-pick
            dfs(curr, i+1)

        dfs([], 0)
        return subarrays


if __name__ == '__main__':
    ob = Solution()
    # arr = list(map(int, input("arr: ").split()))
    arr = ast.literal_eval(input("arr: "))
    ans = ob.sumSubarrayMins(arr)

    print(ans)
