def binarySearchRec(arr, item, l, r):
    mid = (l + r) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:  # item is on left side
        return binarySearchRec(arr, item, l, mid - 1)
    else:
        return binarySearchRec(arr, item, mid + 1, r)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    item = 5
    print(binarySearchRec(arr, item, 0, len(arr) - 1))
