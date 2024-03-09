## [Fractional Knapsack](https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1)

Given weights and values of  **N**  items, we need to put these items in a knapsack of capacity  **W**  to get the  **maximum**  total value in the knapsack.  
**Note:**  Unlike 0/1 knapsack, you are  **allowed**  to break the item here.

### **Example 1:**

#### **Input:** 
N = 3, W = 50 
value[] = {60,100,120}
weight[] = {10,20,30}

#### **Output:** 
240.000000 

#### **Explanation:**  
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 

### **Example 2:**

#### **Input:** 
N = 2, W = 50
value[] = {60,100}
weight[] = {10,20}
#### **Output:** 
160.000000 **Explanation:**Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.

## **Your Task** :

Complete the function **fractionalKnapsack()**  that receives maximum capacity , array of structure/class and size  **N**  and returns a double value representing the maximum value in knapsack.  
**Note:** The details of structure/class is defined in the comments above the given function.

**Expected Time Complexity** : O(NlogN)

**Expected Auxilliary Space**: O(1)

**Constraints:**  
1 <= N <= 10^5  
1 <= W <= 10^9  
1 <= valuei, weighti  <= 10^4

<hr/>

### Sorting approach

```py
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        lst = [[item.value, item.weight, item.value/item.weight] for item in arr]
        lst.sort(key= lambda i: i[2], reverse=True)
        res = 0
        for itm in lst:
            if itm[1] <= W:
                res += itm[0]
                W -= itm[1]
            else:
                res += ((W/itm[1])*itm[0])
                W = 0
        
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends

```


### Max-Heap approach:

```py
import heapq

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # We want item with highest profit_by_weight ratio on top (root of heap)
        max_heap = [[-1 * (item.value/item.weight), item.value, item.weight] for item in arr]
        heapq.heapify(max_heap)
        max_profit = 0
        
        while max_heap:
            profit_by_weight, value, weight = heapq.heappop(max_heap)
            if weight <= W:
                max_profit += value
                W -= weight
            else:
                max_profit += ((W/weight)*value)
                W = 0
        return max_profit
```
