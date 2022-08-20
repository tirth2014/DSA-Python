# Solution - 1 (Using Merge Sort):

class Solution:
    def merge(self, arr, L, R):
        icnt = 0
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1

            elif R[j] < L[i]:
                arr[k] = R[j]
                icnt += len(L) - i
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
        return icnt

    def inversionCount(self, arr, n):      # same as mergeSort
        icnt = 0
        if n > 1:
            mid = n // 2
            L = arr[:mid]
            R = arr[mid:]
            icnt += self.inversionCount(L, len(L))
            icnt += self.inversionCount(R, len(R))
            icnt += self.merge(arr, L, R)

        return icnt


if __name__ == "__main__":
    ob = Solution()
    inp = list(map(int, input().strip().split()))
    ans = ob.inversionCount(inp, len(inp) - 1)
    print(ans)
