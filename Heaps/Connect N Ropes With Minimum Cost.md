
## Problem statement

You have been given 'N' ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.

The test-data is such that the result will fit into a 32-bit integer.

#### Sample Input 1:

```
4
4 3 2 6

```

#### Sample Output 1:

```
29

```

#### Explanation:

```
1) If we first connect ropes of lengths 2 and 3, we will left with three ropes of lengths 4, 6 and 5.

2) Now then, if we connect ropes of lengths 4 and 5, we will left with two ropes of lengths 6 and 9.

3) Finally, we connect the remaining two ropes and all ropes are now connected.

Total cost for connecting all ropes in this way is 5 + 9 + 15 = 29  which is the optimized cost.
Now there are other ways also for connecting ropes. For example, if we connect 4 and 6 first (we get three ropes of lengths 3, 2 and 10), then connect 10 and 3 (we get two ropes of length 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38 which is not the optimal cost

```

#### Sample Input 2:

```
5
1 2 3 4 5

```

#### Sample Output 2:

```
33
```
#### Companies that have asked this question:

Paytm (One97 Communications Limited), PharmEasy, Paypal, Cisco, Optum, Arcesium, Uber, Google, Goldman Sachs, Microsoft, Amazon, Fynd (Shopsense Retail Technologies Ltd.), SpeedLabs, Encore Capital Group, Mindtree, Dell India, Smallcase, Gainsight, Nucleus Software, NCR Corporation, Cloud Analogy.

<hr/>

### Solution:
#### Approach:
Generate a minHeap and take a pair of 2 minimum elements each time, add the sum to res and push to minHeap till minHeap is not empty.

```py
from sys import stdin,setrecursionlimit
import heapq
setrecursionlimit(10**7)

def connectRopes( arr, n) :
	min_heap = arr.copy()
	heapq.heapify(min_heap)
	res = 0

	while min_heap and len(min_heap) > 1:
		first  = heapq.heappop(min_heap)
		second = heapq.heappop(min_heap)
		res += first+second
		heapq.heappush(min_heap, first+second)
	
	return res




#taking input using fast I/O
def takeInput() :
	n = int(input("n: "))

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n


#main
arr, n = takeInput()
print(connectRopes( arr, n))

"""
Example:
  n: 4
  4 3 2 6
  29
"""
```



#### Time Complexity:

-   The time complexity of building the initial min-heap is `O(n)`.
-   Inside the`heapq.heappop()`operation`heapq.heappush()` operation, each of which takes `O(log n)` time.
-   And
-   Therefore, the overall time complexity is `O(n log n)` due to the while loop and the heap operations inside it.
