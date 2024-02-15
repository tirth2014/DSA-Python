
*There are many different versions of quickSort partition algorithm that pick pivot in different ways.*

> 1.  Always pick the first element as a pivot
> 2.  Always pick the last element as a pivot
> 3.  Pick a random element as a pivot
> 4.  Pick median as a pivot

</br>

```py
import random
import ast


def partition(nums, start, end):
    pivot_ind = random.randint(start, end)
    pivot = nums[pivot_ind]
    nums[pivot_ind], nums[start] = nums[start], nums[pivot_ind]  # Swap pivot with start

    pindex = start + 1

    for i in range(start + 1, end + 1):
        if nums[i] <= pivot:
            nums[i], nums[pindex] = nums[pindex], nums[i]
            pindex += 1

    nums[start], nums[pindex - 1] = nums[pindex - 1], nums[start]  # Swap pivot back
    return pindex - 1

arr = ast.literal_eval(input("arr: "))
print('partition idx: ', partition(arr, 0, len(arr)-1))
print(arr)
```
### Input
arr: `[3,2,1,5,6,4]`

### Output

pivot idx:  `3` &nbsp; pivot:  `5` &nbsp; partition idx:  `4` &nbsp; arr: `[4, 2, 1, 3, 5, 6]`

### Input
arr: `[3,2,1,5,6,4]`

### Output

pivot idx:  `4` &nbsp; pivot:  `6` &nbsp; partition idx:  `5` &nbsp; arr: `[4, 2, 1, 5, 3, 6]`


### Input
arr: `[3,2,1,5,6,4]`

### Output

pivot idx:  `2` &nbsp; pivot:  `1` &nbsp; partition idx:  `0` &nbsp; arr: `[1, 2, 3, 5, 6, 4]`


```py
import random
import ast


def partition(nums, start, end):
    pivot_ind = random.randint(start, end)
    pivot = nums[pivot_ind]
    nums[pivot_ind], nums[end] = nums[end], nums[pivot_ind]

    pindex = start

    for i in range(start, end + 1):
        if nums[i] > pivot:
            nums[i], nums[pindex] = nums[pindex], nums[i]
            pindex += 1

    nums[end], nums[pindex] = nums[pindex], nums[end]
    return pindex

arr = ast.literal_eval(input("arr: "))
print('partition idx: ', partition(arr, 0, len(arr)-1))
print(arr)
```

### Input
arr: `[3,2,1,5,6,4]`

### Output

pivot_ind: `1` &nbsp; pivot: `2`  &nbsp; partition idx:  `4` &nbsp; arr: `[3, 4, 5, 6, 2, 1]`
