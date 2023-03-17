"""
The algorithm maintains two subarrays in a given array.

The subarray which already sorted. 
The remaining subarray was unsorted.
In every iteration of the selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the beginning of the unsorted subarray. 

After every iteration sorted subarray size increase by one and the unsorted subarray size decrease by one.

Time Complexity: The time complexity of Selection Sort is O(N^2) as there are two nested loops:

One loop to select an element of Array one by one = O(N)
Another loop to compare that element with every other Array element = O(N)
Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N^2)

Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. 
The selection sort never makes more than O(N) swaps and can be useful when the memory write is a costly operation. 
"""

#selection sort
import sys

def selSort(arr,n):
    for i in range(n):
        currMin = sys.maxsize
        for j in range(i,n):
            if arr[j] < currMin:
                currMin=arr[j]
                ind=j
        arr[i],arr[ind] = arr[ind],arr[i]
    return arr
def main():
    lst=[]
    n=int(input())
    for i in range(n):
        lst.append(int(input()))
    print('original list: ', lst)
    print('sorted list: ',selSort(lst,n))

main()
