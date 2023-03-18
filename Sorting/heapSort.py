"""
Heapify: Heapify is an algorithm used to build a heap data structure from an array. 
A heap is a specialized binary tree-based data structure that satisfies the heap property, which states that the parent node is always greater than or equal to (in a max-heap) or less than or equal to (in a min-heap) its children nodes.
The heapify algorithm takes an array and reorders its elements so that they form a heap. 
It works by starting from the middle of the array and iterating backwards through its elements, calling the sift-down operation on each one. 
The sift-down operation compares the current node with its children nodes, and if necessary, swaps it with the larger (in a max-heap) or smaller (in a min-heap) child node, and continues recursively until the heap property is satisfied.
Heapify is an efficient algorithm, with a time complexity of O(n), where n is the length of the array. 
This is because it only needs to perform the sift-down operation on the non-leaf nodes of the binary tree, which are roughly half of the total number of nodes.

=> Why heapify starts from middle of an array?
Heapify starts from the middle of the array and not from the beginning (index 0) because of the way that heaps are represented as binary trees in memory.

If we start heapify from the last non-leaf node and work our way backwards towards the root, we ensure that the children of every node we visit have already been heapified. 
This is because we're moving from the bottom-up in the tree, and we're heapifying the nodes as we go.
This makes the algorithm more efficient, because we only need to perform the sift-down operation on the non-leaf nodes of the binary tree.
If we started at index 0 and worked our way forwards, we would be heapifying nodes whose children have not yet been heapified, which could lead to violations of the heap property.
"""

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
