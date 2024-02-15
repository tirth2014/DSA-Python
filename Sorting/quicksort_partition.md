
*There are many different versions of quickSort partition algorithm that pick pivot in different ways.*

> 1.  Always pick the first element as a pivot
> 2.  Always pick the last element as a pivot
> 3.  Pick a random element as a pivot
> 4.  Pick median as a pivot

</br>

## 1.

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

</br>
</br>

## 2.

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

</br>
</br>

## 3.

```py
import ast


def partition(arr, start, end):
    # Choose a pivot
    # Here, we're setting first element as pivot
    pivot_idx = start
    pivot = arr[pivot_idx]

    # initialize i and j as the start and end indices of the array
    i, j = start, end

    # loop until j crosses i
    while i < j:
        # find element greater than pivot from left(start)
        # jya sudhi element>pivot na male tya sudhi i ne increment karta rehvanu
        while arr[i] <= pivot and i <= end - 1:
            i += 1

        # Find element smaller than pivot from right(end)
        # jya sudhi element <= pivot na male tya sudhi j ne decrement karta rehvanu
        while arr[j] > pivot and j >= start + 1:
            j -= 1

        # if j hasn't crossed i yet and if we find both elements i.e. greater on left and smaller on right of pivot then swap them
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot element with element at index j (partition index)
    # All elements on subarray  left of partition index are smaller and right of it are greater
    # so the partition index is correct position for our pivot.
    arr[start], arr[j] = arr[j], arr[start]
    # return the partition index
    return j

arr = ast.literal_eval(input("arr: "))
print('partition idx: ', partition(arr, 0, len(arr)-1))
print(arr)
```

### Input
arr: `[3,2,1,5,6,4]`

### Output

pivot_ind: `1` &nbsp; pivot: `2`  &nbsp; partition idx:  `2` &nbsp; arr: `[1, 2, 3, 5, 6, 4]`
