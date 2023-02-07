def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # Floor division of length of array
        L = arr[:mid]        
        R = arr[mid:]
        
        # Recursively call mergeSort function on left and right subarrays respectively till array is not broken in singleton elements.
        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
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


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("The Array before MergeSort: ")
    print(arr)
    mergeSort(arr)
    print("The Array after MergeSort: ")
    print(arr)
