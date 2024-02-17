## Replace Each Element Of Array With Its Corresponding Rank
### Problem statement

Given an array of integers  _**'ARR’**_  of size  _**‘N’**_. Replace each element of this array with its corresponding rank and return the array.

  

The rank of an element is an integer between 1 to ‘N’ inclusive that represents how large the element is in comparison to other elements of the array. The following rules can also define the rank of an element:

  

```
1. It is an integer starting from 1.
2. The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
3. It should be as small as possible.

```

**For Example:**

```
'ARR' = [4, 7, 2, 90]
Here, 2 is the smallest element, followed by 4, 7, and 90. 
Hence rank of element 2 is 1, element 4 is 2, element 7 is 3, and element 90 is 4.
Hence we return [2, 3, 1, 4].
```

### Approach-1 (Sorting)
**Time Complexity: O(N^2)**  </br>
Gives TLE for some cases
```py
from typing import List

def replaceWithRank(arr: List[int], n : int) -> List[int]:
    sorted_arr = sorted(list(set(arr)))
    for i in range(n):
        arr[i] = sorted_arr.index(arr[i]) + 1
    return arr
```

<hr/>

### Approach-2 (Optimized Sorting)

```py
from typing import List

def replaceWithRank(arr: List[int], n : int) -> List[int]:

    # O(nlogn) for sorting an array
    rank, sorted_arr, map = 1, sorted(arr), {}

    # O(n)
    for el in sorted_arr:
        if el not in map:
            map[el] = rank
            rank += 1

    # O(n)
    for i in range(n):
        arr[i] = map[arr[i]]

    return arr
```

<hr/>

### Approach-3 (Min Heap)

```python
import ast
import heapq
from typing import List

def replaceWithRank(arr: List[int], n : int) -> List[int]:
    min_heap = []
    for i, el in enumerate(arr):
        # We must put el first because min-heap will be build based on the first element of array
        heapq.heappush(min_heap, [el, i])
    rank, prev = 0, float('-inf')
    for _ in range(n):
        curr = heapq.heappop(min_heap)
        if curr[0] != prev:
            arr[curr[1]] = rank + 1
            rank += 1
        else:
            arr[curr[1]] = rank
        prev = curr[0]
    return arr


arr = ast.literal_eval(input("arr: "))
print('res: ', replaceWithRank(arr, len(arr)))
```
### Example:
#### Input:
> arr: [1, 2, 6, 9, 2]
#### Output:
> res:  [1, 2, 3, 4, 2]

### Analysis:

The time complexity of the `replaceWithRank` function can be analyzed as follows:

1.  Building the min-heap: We iterate through the input list `arr` of size `n`, and for each element, we perform a `heappush` operation onto the `min_heap`. This operation takes O(log n) time. Since we perform this operation for all `n` elements, the total time complexity for building the min-heap is O(n log n).
    
2.  Processing the min-heap: We iterate `n` times, each time performing a `heappop` operation from the `min_heap`. The `heappop` operation takes O(log n) time. Thus, the total time complexity for processing the min-heap is O(n log n).
    

Overall, the dominant factor in the time complexity is the building and processing of the min-heap, both of which contribute O(n log n) to the total time complexity.

So, the time complexity of the `replaceWithRank` function is **`O(n log n)`**. This function efficiently replaces the elements of the input list `arr` with their ranks while maintaining the relative order of equal elements
