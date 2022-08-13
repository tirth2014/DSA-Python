def binarySearch(arr, item):
    l = 0
    r = len(arr) - 1
    while l != r:
        mid = (l + r) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:  # item is on left side
            r = mid - 1
        else:
            l = mid + 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    item = 5
    print(binarySearch(arr, item))
