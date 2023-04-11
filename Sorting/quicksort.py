class Solution:

    # function to partition the array
    def partition(self,arr,low,high):
        # Choose a pivot
        # Here, we're setting first element as pivot
        pivot = low

        # initialize i and j as the start and end indices of the array
        i,j = low,high

        # loop until j crosses i
        while i<j:
            # find element greater than pivot from left(low)
            # jya sudhi element>pivot na male tya sudhi i ne increment karta rehvanu
            while arr[i] <= arr[pivot] and i <= high-1:
                i+=1

            # Find element smaller than pivot from right(high)
            # jya sudhi element <= pivot na male tya sudhi j ne decrement karta rehvanu
            while arr[j] > arr[pivot] and j >= low+1:
                j-=1

            # if j hasn't crossed i yet and if we find both elements i.e. greater on left and smaller on right of pivot then swap them 
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]

        # Swap pivot element with element at index j (partition index)
        # All elements on subarray  left of partition index are smaller and right of it are greater
        # so the partition index is correct position for our pivot.
        arr[pivot],arr[j] = arr[j],arr[pivot]
        # return the index of pivot element
        return j

    def quicksort(self,arr,low,high):
        # base case: when the array has more than one element
        if low<high:
            # Place a pivot at it's correct place
            pI = self.partition(arr,low,high)  # partition_ind

            # Recursively perform quicksort on pivot's left and right sub-arrays
            self.quicksort(arr,low,pI-1)
            self.quicksort(arr,pI+1,high)


ob = Solution()
arr = [4,6,2,5,7,9,1,3]
print(f"Array Before Quick Sort: {arr}")
# perform quick sort on the array
ob.quicksort(arr,0,len(arr)-1)
print(f"Array After Quick Sort: {arr}")  # [1, 2, 3, 4, 5, 6, 7, 9]


# The time complexity of the quicksort algorithm is O(nlogn) in the average case and O(n^2) in the worst case, where n is the size of the input array. 
# The worst case occurs when the pivot element chosen is either the smallest or largest element in the array, 
# resulting in one sub-array having n-1 elements and the other sub-array having 0 elements.

# The space complexity of the quicksort algorithm is O(logn) in the average case and O(n) in the worst case. 
# The space complexity is determined by the depth of the recursion tree, which is logn in the average case and 
# n in the worst case when the partition function always picks the smallest or largest element as the pivot.

# However, in the implementation of the quicksort algorithm shown in the code above, the worst case can be avoided by using a randomized pivot selection method instead of always choosing the first element as the pivot. 
# With randomized pivot selection, the average time complexity remains O(nlogn) and the worst case time complexity becomes extremely rare.



# RANDOMIZED:

import random

class Solution:
    
    def partition(self,arr,low,high):
        rand_int = random.randint(low,high)  # Choose random index from low to high
        arr[low],arr[rand_int] = arr[rand_int],arr[low]   # Swap first index element with randomly selected element to make the flow easy
        pivot = low
        i,j = low,high

        # loop until j crosses i
        while i<j:
            while arr[i] <= arr[pivot] and i <= high-1:
                i+=1
            while arr[j] > arr[pivot] and j >= low+1:
                j-=1

            if i<j:
                arr[i],arr[j] = arr[j],arr[i]

        arr[pivot],arr[j] = arr[j],arr[pivot]
        return j

    def quicksort(self,arr,low,high):
        # base case: when the array has more than one element
        if low<high:
            pI = self.partition(arr,low,high)
            self.quicksort(arr,low,pI-1)
            self.quicksort(arr,pI+1,high)


ob = Solution()
arr = [1,2,3,4,5,6,7]
print(f"Array Before Quick Sort: {arr}")
ob.quicksort(arr,0,len(arr)-1)
print(f"Array After Quick Sort: {arr}")  # [1, 2, 3, 4, 5, 6, 7, 9]
