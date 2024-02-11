## Implement a priority queue
#### [Problem Link](https://www.codingninjas.com/studio/problems/implement-a-priority-queue-_1743878?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM)
<br/>
You have to implement the pop function of Max Priority Queue and implement using a heap.
<br/>
<br/>


**Functions :**

```
a) push(int x) : 'x' has to be inserted in the priority queue. This has been implemented already

b) pop() : return the maximum element in the priority queue, if priority queue is empty then return '-1'.

```

  

**Example:**

```
We perform the following operations on an empty priority queue:

When operation push(5) is performed, we insert 1 in the priority queue.

When operation push(2) is performed, we insert 2 in the priority queue. 

When operation pop() is performed, we remove the maximum element from the priority queue and print which is 5.

When operation push(3) is performed, we insert 1 in the priority queue.

When operation pop() is performed, we remove the maximum element from the priority queue and print which is 3.
```

### Detailed explanation ( Input/output format, Notes, Images )

**Input Format:**

```
The first line of contains a single integer, ‘n’ , representing the  number of operations.

The next ‘n’ lines of each test case contain operations that have to be performed on the stack. 

Operations of the format
1 x : denotes to perform the operation push(x).
2 : denotes to perform the operation pop(). 

```


**Sample Input 1 :**

```
8
1 4
1 9
2 
1 5
2 
1 10
1 1
2 
```


**Sample Output 1 :**

```
9
5
10
```


**Explanation For Sample Output 1 :**


After processing 1 4
The elements in the priority queue are 4

After processing 1 9
The elements in the priority queue are 4,9

After processing 2
The largest element which is 9 is printed and removed from the queue
The elements in the priority queue are 4

After processing 1 5
The elements in the priority queue are 4,5

After processing 2
The largest element which is 5 is printed and removed from the queue

After processing 1 10
The elements in the priority queue are 4,10

After processing 1 1
The elements in the priority queue are 1,4,10

After processing 2
The largest element which is 10 is printed and removed from the queue
The elements in the priority queue are 1,4



**Sample Input 2 :**

```
8
2 
1 6
2 
2 
2 
1 2
1 9
1 5

```

**Sample Output 2 :**

```
-1
6
-1
-1

```

**Constraints :**

```
1 <= n <= 10^6

Time Limit: 1 sec
```


### Solution

```python
from typing import List

def heapify(heap):
    # Heapify the heap to maintain the max-heap property for all nodes
    # i.e. All parent nodes must be greater than their child nodes
    ptr = largest = 0
    
    while True:
        left_child = (ptr*2) + 1
        right_child = (ptr*2) + 2
        
        if left_child < len(heap) and heap[left_child] > heap[largest]:
            largest = left_child

        if right_child < len(heap) and heap[right_child] > heap[largest]:
            largest = right_child

        if largest != ptr:
            heap[ptr], heap[largest] = heap[largest], heap[ptr]
            ptr = largest
        
        else:
            break


def pop(heap: List[int]) -> int:
    if not heap:
        return -1
    elif len(heap) == 1:
        return heap.pop()

    # Replace max element (first) with last element (leaf)
    heap[0], heap[-1] = heap[-1], heap[0]

    # Store max elem. to return at last
    max_elem = heap.pop()
    
    heapify(heap)
    
    return max_elem

'''
    def push(self, x):
        self.heap.append(x)
        pos = len(self.heap) - 1
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[pos] > self.heap[parent]:
                self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
                pos = parent
            else:
                break
'''
```
