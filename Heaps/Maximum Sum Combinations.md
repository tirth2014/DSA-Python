
# [Maximum Sum Combinations](https://www.interviewbit.com/problems/maximum-sum-combinations/)
[Heaps And Maps](https://www.interviewbit.com/courses/programming/topics/heaps-and-maps)

## **Problem Description**

  

Given two equally sized 1-D arrays **A, B** containing **N** integers each.

A **sum combination** is made by adding one element from array **A** and another element of array **B**.

Return the **maximum C valid sum combinations** from all the possible sum combinations.

  
  

### **Problem Constraints**

1 <= N <= 10^5 </br>

1 <= A[i] <= 10^5 </br>

1 <= C <= N </br>

  
  

### Input Format

First argument is an one-dimensional integer array **A** of size **N**.

Second argument is an one-dimensional integer array **B** of size **N**.

Third argument is an integer **C**.

  
  

### **Output Format**

Return a one-dimensional integer array of size **C** denoting the top C maximum sum combinations.

**NOTE:**

The returned array must be sorted in non-increasing order.

  
  

### **Example Input**

Input 1: </br>

 A = [3, 2] </br>
 B = [1, 4] </br>
 C = 2 </br></br>

Input 2: </br>

 A = [1, 4, 2, 3] </br>
 B = [2, 5, 1, 6] </br>
 C = 4 </br>

  
  

### **Example Output**

Output 1: </br>

 [7, 6]  </br></br>

Output 2:    </br>

 [10, 9, 9, 8]

  
  

### **Example Explanation**

#### Explanation 1:

 7  &nbsp; &nbsp;    (A : 3) + (B : 4) </br>
 6   &nbsp; &nbsp;   (A : 2) + (B : 4) </br>

#### Explanation 2:

 10 &nbsp;   (A : 4) + (B : 6)  </br>
 9  &nbsp; &nbsp;   (A : 4) + (B : 5) </br>
 9  &nbsp; &nbsp;   (A : 3) + (B : 6) </br>
 8  &nbsp; &nbsp;  (A : 3) + (B : 5) 

<hr/>

## Solution (Sort + MaxHeap + HashSet Approach):

```py
import heapq

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers

    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        maxHeap, res, n, idx_done = [], [], len(A) - 1, set()
        maxHeap.append([-(A[0] + B[0]), (0, 0)])
        idx_done.add((0, 0))

        while C > 0:
            top = heapq.heappop(maxHeap)  # extract max sum pair - [sum, indices pair]
            res.append(-top[0])  # push sum of max sum combination pair in res
            C -= 1
            i, j = top[1][0], top[1][1]

            if i < n and j < n:
                # keep checking diagonals
                if (i + 1, j) not in idx_done:
                    heapq.heappush(maxHeap, [-(A[i + 1] + B[j]), (i + 1, j)])
                    idx_done.add((i + 1, j))
                if (i, j + 1) not in idx_done:
                    heapq.heappush(maxHeap, [-(A[i] + B[j + 1]), (i, j + 1)])
                    idx_done.add((i, j + 1))

        return res


if __name__ == '__main__':
    ob = Solution()
    arr1 = ast.literal_eval(input("arr1: "))
    arr2 = ast.literal_eval(input("arr2: "))
    k = int(input("C: "))
    ans = ob.solve(arr1, arr2, C)
    print('\nans', ans)
```

## Approach:
- First `sort` both the arrays `A` and `B` to make things easier. (Here, we have sorted in non-increasing order)
- Create MaxHeap initialized with the first item:  sum of the first elements of both the sorted list and pair of their index (because, we know that it's the max. possible sum pair, for sure.)
  - i.e., `[-(A[0]+B[0]), (0,0)]`
  - We will be adding the sum of pairs with a `negative sign` to treat the heap as a MaxHeap, as Python's default is MinHeap using `heapq` module.
- Now, till we don't get `C` max. sum combinations in our result list we will do the following:
  - top = `heappop` max item from MaxHeap
  - add sum, `-top[0]` in result and extract `i`, `j`  index of MaxSum pair and add `(i,j)` to `idx_done` set.
  - `idx_done` HashSet used to track which indices pairs sum are already added in result, to avoid duplication.
  - now, if `i` and `j` both are in the range of `n` then `heappush` diagonals pairs sum and indices. as well as add indices to `idx_done`.
- Finally, return result.

<hr/>

## Detailed Approach & Complexity Analysis:
[Video Explanation](https://www.youtube.com/watch?v=yNLu2kJUjjU&pp=ygUYTWF4aW11bSBTdW0gQ29tYmluYXRpb25z) </br>

This solution aims to find the top C pairs of numbers, where each pair consists of one number from list A and one number from list B, such that their sum is the maximum among all possible pairs.

Here's how the approach works:

1. **Initialization**:
   - The lists A and B are sorted in descending order to ensure that the maximum elements are considered first.
   - A max heap (`maxHeap`) is initialized to store pairs of sums and their corresponding indices.
   - The maximum sum pair of the initial elements of lists A and B is computed and added to the `maxHeap`. The negative sum is stored in the heap to simulate a max heap using a min heap provided by heapq in Python.
   - The indices of the processed elements are stored in a set `idx_done` to avoid processing the same indices again.

2. **Main Loop**:
   - While there are still pairs to find (`C > 0`), the top element (max sum pair) is popped from the `maxHeap`.
   - The negative of the sum is appended to the result list `res`.
   - The indices of the popped pair are retrieved.
   - If there are more elements in lists A and B to explore, new pairs are formed by moving one step right or one step down along the diagonal.
   - These new pairs are added to the `maxHeap`, and their indices are stored in `idx_done`.

3. **Return**:
   - Once the top C pairs have been found, the list `res` containing the sums of these pairs is returned.

4. **Time Complexity**:
   - Sorting the lists `A` and `B` takes `O(N log N)`, where `N` is the length of the lists.
   - The main loop runs `C` times. Inside the loop, each operation (heap pop, heap push, set lookup) takes `O(log C)` time.
   - Therefore, the overall time complexity is `O((N + C) log C)`.

5. **Space Complexity**:
   - The space complexity is `O(N)` for storing the max heap, result list, and set of indices.
   - Additionally, sorting the lists in place requires no extra space.
   - Hence, the overall space complexity is `O(N)`.
