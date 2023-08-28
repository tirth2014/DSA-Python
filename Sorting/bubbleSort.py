# Time Complexity: O(N^2)
# Auxiliary Space: O(1) 

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already sorted
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


if __name__ == "__main__":
    arr = list(map(int,input().strip().split(',')))
    n = len(arr)
    print('---Array before sorting',arr)
    res = bubbleSort(arr)
    print('---Array after bubble sorting',res)
    

# Optimized Bubble Sort
# The above function always runs O(N^2) time even if the array is sorted. 
# It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap. 

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
            
    return arr

# Worst and Average Case Time Complexity: O(N2). The worst case occurs when an array is reverse sorted.
# Best Case Time Complexity: O(N). The best case occurs when an array is already sorted.
# Auxiliary Space: O(1)

