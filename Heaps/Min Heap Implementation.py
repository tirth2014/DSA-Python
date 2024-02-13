"""
Min Heap Implementation
https://www.codingninjas.com/studio/problems/min-heap-implementation_5480527?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM&customSource=studio_nav

Problem statement:

Implement the Min Heap data structure.

Min heap is a tree data structure (a complete binary tree) where the root element is the smallest of all the elements in the heap. Also, the children of every node are smaller than or equal to the root node. 

The insertion and removal of elements from the heap take log('N'), where 'N' is the number of nodes in the tree. 

Implement the “minHeap” class. You will be given the following types of queries:-

0 extractMinElement(): Remove the minimum element present in the heap, and return it.

1 deleteElement( i ): Delete the element present at the 'i' th index.

2 insert( key ): Insert the value 'key' in the heap.

For queries of types 0 and 1, at least one element should be in the heap.
"""

class MinHeap:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.heap = [0] * capacity

    def heapify(self, i):
        smallest = i
        left_child = 2*i+1
        right_child = 2*i+2
        if left_child < self.size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < self.size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def shift_up(self, i):
        # move up the element from bottop to top
        while i >= 0:
            parent = (i-1)//2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
            

    def extractMinElement(self):            
        if self.size == 0:
            return -1
        min_elem = self.heap[0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1
        self.heapify(0) 
        return min_elem

    def deleteElement(self, ind):
        if ind >= self.size: 
            return
            
        self.heap[ind], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[ind]
        self.size -= 1
        self.heapify(ind)

    def insert(self, val):        
        if self.size == self.capacity:
            return
        self.heap[self.size] = val
        self.size += 1
        idx = self.size - 1
        self.shift_up(idx)
        
