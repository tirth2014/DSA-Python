# Inversion Count:
# For an array, inversion count indicates how far (or close) the array is from being sorted.
# If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

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
