#https://www.codingninjas.com/studio/problems/convert-min-heap-to-max-heap_1381084?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from typing import List

def minToMaxHeap(n: int, heap: List[int]) -> List[int]:
    
    def heapify(i):
        largest = i
        left_child = 2*i+1
        right_child = 2*i+2

        if left_child < n and heap[left_child] > heap[largest]:
            largest = left_child
        
        if right_child < n and heap[right_child] > heap[largest]:
            largest = right_child

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            heapify(largest)

    # call heapify for all internal nodes
    for idx in range (((n-2)//2), -1, -1):
        heapify(idx)


    return heap
