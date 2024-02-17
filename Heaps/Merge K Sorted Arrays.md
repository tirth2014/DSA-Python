### [Problem Link](https://www.codingninjas.com/studio/problems/merge-k-sorted-arrays_975379?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM)

### Approach-1 [Not so optimal min-heap approach]
```py
import heapq
import ast

def mergeKSortedArrays(kArrays, k:int):
	# kArrays is a list of 'k' lists.
	# Return a list.
	merged = [y for x in kArrays for y in x]
	heapq.heapify(merged)
	res = []
	n = len(merged)
	for _ in range(n):
		res.append(heapq.heappop(merged))
	return res
```
<hr/>

### Approach-2 [Min Heap - Optimal]


```py
import heapq

def mergeKSortedArrays(kArrays, k:int):

	min_heap, res = [], []
	for arr_idx in range(k):
		heapq.heappush(min_heap, [kArrays[arr_idx][0], arr_idx, 0])

	while min_heap:
		curr = heapq.heappop(min_heap)

		arr_idx = curr[1]  # array index
		ele_idx = curr[2]  # element index

		res.append(curr[0])
		if ele_idx+1 < len(kArrays[arr_idx]):
			heapq.heappush(min_heap, [kArrays[arr_idx][ele_idx+1], arr_idx, ele_idx+1])

	return res
```
</br>

### Analysis
 
1.  **Building the initial min heap:**
    
    -   We initially push the first element from each array into the heap. This operation takes `O(k log k)` time, where `k` is the number of arrays. Since each array is considered once, and inserting into the heap takes `O(log k)` time for each element.
2.  **While loop for merging:**
    
    -   In each iteration of the while loop, we pop an element from the heap, which takes `O(log k)` time.
    -   We also append the popped element to the result list, which takes `O(1)` time.
    -   If the popped element is not the last element in its corresponding array, we push the next element from that array into the heap. Pushing into the heap takes `O(log k)` time.
3.  **Total time complexity:**
    
    -   The overall time complexity of the while loop depends on the total number of elements across all arrays. Let's denote this total number of elements as `n`.
    -   Since each element is pushed and popped from the heap at most once, the total time complexity for heap operations inside the while loop is `O(n log k)`.

Combining the time complexity of building the initial heap and the while loop, the overall time complexity is `O(k log k + n log k)`, and can be approximated as `O(n log k)`.


<hr/>

### Approach-3 [k-way Merge Sort]

The time complexity of the provided `mergeKSortedArrays` function, which uses a recursive merge sort approach, can be analyzed as follows:

1.  **Divide and Conquer Strategy**:
    
    -   The function divides the array of `k` sorted arrays into halves recursively until it reaches arrays of size `1` or `2`.
    -   Each level of recursion divides the problem size by `2`.
2.  **Merge Operation**:
    
    -   At each level of recursion, the `merge` function is called to merge two sorted arrays.
    -   The `merge` operation takes `O(n)` time, where `n` is the total number of elements in the two arrays being merged.
3.  **Number of Levels**:
    
    -   The number of levels in the recursion tree is `O(log k)`, where `k` is the number of input arrays.
4.  **Overall Time Complexity**:
    
    -   At each level of recursion, there are `O(k)` merge operations, each taking `O(n)` time.
    -   Since there are `O(log k)` levels, the overall time complexity is `O(k * n * log k)`.

Therefore, the time complexity of the `mergeKSortedArrays` function is `O((n*k) * log(k))`, where `k` is the number of input arrays and `n` is the average number of elements in each array.

```py
import ast

def merge(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res


def merge_sort_recursively(kArrays, start, end):
    # If there's only one array
    if start == end:
        return kArrays[start]

    # If there are only 2 arrays, merge them directly
    if start + 1 == end:
        return merge(kArrays[start], kArrays[end])

    # If there are more than 2 arrays
    mid = start+(end-start)//2

    # Divide the array into two halves
    arr1 = merge_sort_recursively(kArrays, start, mid)
    arr2 = merge_sort_recursively(kArrays, mid+1, end)

    # Return the final merged array
    return merge(arr1,arr2)


def mergeKSortedArrays(kArrays, k: int):
    return merge_sort_recursively(kArrays, 0, k - 1)


arr = ast.literal_eval(input("arr: "))
print('res: ', mergeKSortedArrays(arr, len(arr)))
```
#### Example:
**Input**
arr = [1,3,9], [2,6,7], [2,8,10], [9,10,11], [1,2,8] </br>
**Output**
res:  [1, 1, 2, 2, 2, 3, 6, 7, 8, 8, 9, 9, 10, 10, 11]
