"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. 
-> If two asteroids meet, the smaller one will explode. 
-> If both are the same size, both will explode. 
-> Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
[-2,1,1,-1]
Output: [-2,1] 

Example 5:
[-2,5,3,-4,-6,8]
Output: [-2,-6,8] 

Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

# Time Complexity: O(N)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            to_push, neg_pos, flag = True, False, False
            if stack:
                neg_pos = ((num < 0) and (stack[-1] > 0))

            while stack and neg_pos and abs(num) >= stack[-1]:
                if stack.pop() == abs(num):
                    flag = True
                    break
                neg_pos = stack and ((num < 0) and (stack[-1] > 0))
            if flag: continue
            if stack and neg_pos and abs(num) < stack[-1]:
                to_push = False

            if to_push:
                stack.append(num)

        return stack


# Logic same but more readable and a little more efficient
# We eliminate unnecessary variables (neg_pos and flag) to simplify the code.
# We use a single while loop to handle the asteroid collisions more concisely.
# We use the else clause with the while loop to handle the case when no collisions occur, which makes the code more readable.
# Imp. thing to learn...In python we can use: (while...else)
import ast
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Initialize an empty stack to track surviving asteroids
        # -ve goes down(left) and +ve goes up(right) in stack
        # So, collision is possible only when (+ve asteroid ni upar -ve asteroid) aave
        stack = []

        for num in asteroids:
            # Check for possible collision when a negative asteroid meets a positive one
            while stack and num < 0 < stack[-1]:
                if stack[-1] < abs(num):
                    stack.pop()
                    continue
                # If they have equal absolute values, both asteroids are destroyed
                # only in this case break statement will be executed
                elif stack[-1] == abs(num):
                    stack.pop()
                # Break the loop when no further collisions are possible
                break
            else:
                # If no collision occurred, add the asteroid to the stack
                stack.append(num)

        # The stack now contains the surviving asteroids
        return stack


if __name__ == '__main__':
    ob = Solution()
    # arr = list(map(int, input("arr: ").split()))
    for t in range(int(input("#testcases: "))):
        arr = ast.literal_eval(input("arr: "))
        ans = ob.asteroidCollision(arr)
        print(ans)
