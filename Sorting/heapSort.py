def heapify(arr, N, i):
    largest = i  # i = root
    l = 2 * i + 1
    r = 2 * i + 2
    # left child = 2*i + 1
    # right child = 2*i + 2

    # See if left child of root exist and is greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exist and is greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root ONLY IF NEEDED:
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)


def heapSort(arr):
    N = len(arr)
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements from max-heap to last position and decrease the heap size by 1
    for i in range(N - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("The Array before heapSort: ")
    print(arr)
    heapSort(arr)
    print("The Array after heapSort: ")
    print(arr)
