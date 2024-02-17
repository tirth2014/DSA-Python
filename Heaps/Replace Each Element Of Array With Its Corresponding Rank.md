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

### Approach-1
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
