# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

# Characteristics of Insertion Sort:
# This algorithm is one of the simplest algorithm with simple implementation
# Basically, Insertion sort is efficient for small data values
# Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.
# Insertion Sort is in-place(doesn't take extra memory) and stable (preserves order) algorithm.

# ***To sort an array of size N in ascending order:*** 

# Iterate from arr[1] to arr[N] over the array. 
# Compare the current element (key) to its predecessor. 
# If the key(curr) element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

#Insertion Sort 
def main():
    arr = []
    n = int(input())
    while len(arr) != n:
        item = list(map(int, input().split()))
        arr.extend(item)
        print('unsorted array is: ',arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    print('sorted array is: ',arr)


main()


# Time Complexity: O(N^2) 
# Auxiliary Space: O(1)
