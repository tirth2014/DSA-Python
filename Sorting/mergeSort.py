"""
Merger sort is not in-place (requires extra memory space) and it's stable (preserves order) algorithm

Analysis of Merge Sort:
A merge sort consists of several passes over the input. The first pass merges segments of size 1, 
the second merges segments of size 2, and the i_{th} pass merges segments of size 2^i-1. 
Thus, the total number of passes is [log2n]. As merge showed, we can merge two sorted segments in linear time, which means that each pass takes O(n) time.
Since there are [log2n] passes, the total computing time is O(nlogn).
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # Floor division of length of array
        L = arr[:mid]        
        R = arr[mid:]
        
        # Recursively call mergeSort function on left and right subarrays respectively till array is not broken in singleton elements.
        mergeSort(L)
        mergeSort(R)
       
        # Merge Step:
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any element was left
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
