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
