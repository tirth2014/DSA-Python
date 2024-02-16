[Problem Link](https://www.codingninjas.com/studio/problems/merge-k-sorted-arrays_975379?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM)

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
    
    -   We initially push the first element from each array into the heap. This operation takes O(k log k) time, where k is the number of arrays. Since each array is considered once, and inserting into the heap takes O(log k) time for each element.
2.  **While loop for merging:**
    
    -   In each iteration of the while loop, we pop an element from the heap, which takes O(log k) time.
    -   We also append the popped element to the result list, which takes O(1) time.
    -   If the popped element is not the last element in its corresponding array, we push the next element from that array into the heap. Pushing into the heap takes O(log k) time.
3.  **Total time complexity:**
    
    -   The overall time complexity of the while loop depends on the total number of elements across all arrays. Let's denote this total number of elements as n.
    -   Since each element is pushed and popped from the heap at most once, the total time complexity for heap operations inside the while loop is O(n log k).

Combining the time complexity of building the initial heap and the while loop, the overall time complexity is O(k log k + n log k), and can be approximated as O(n log k).
