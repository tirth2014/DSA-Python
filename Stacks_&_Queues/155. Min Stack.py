# 155. Min Stack

# Very noob approach
# Using 2 stacks
class MinStack:

    def __init__(self):
        self.stk = []
        self.temp_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def getMin(self) -> int:
        cur_min = float('inf')
        while self.stk:
            popped = self.stk.pop()
            self.temp_stk.append(popped)
            cur_min = cur_min if popped > cur_min else popped
        self.stk.extend(self.temp_stk[::-1])
        self.temp_stk = []
        return cur_min




# Naive approach:
# Pushing tuple of (val, mini) instead of only val in stack
"""
T.C : O(1)
S.C : O(2N)
"""
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val,val))
        else:
            top_min = self.stk[-1][1]
            self.stk.append((val, val if val < top_min else top_min))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]




      
# Optimal Approach      
"""
155. Min Stack
https://leetcode.com/problems/min-stack/description/

T.C : O(1)
S.C : O(N)

Formula (1) ----> (2 * val) - mini

Ex:
push -2....mini = -2, top = -2
push  0....mini = -2, top =  0
push -3....mini = -3, top = (2 * val) - mini
                          = (2 * -3) - (-2) = -6+2
                          = -4
push 2....mini = -3, top = 2
pop.......popped 2, stack = [-2, 0, -4], mini = -3
          Here, popped st.top element 2 is > mini...So, no need to do anything, just pop
pop.......popped -4, stack = [-2, 0], mini = -3
          Here, popped st.top ele. -4 is < mini...So, we know for sure that it's modified value
          Now, We NEED TO ROLLBACK mini to prev. mini...How?...using formula (1)
          st.top = (2 * val) - mini
          Here, val is our current mini and mini is the prev. mini that we want and st.top is modified val
          i.e. st.top = (2 * mini) - prev. mini
          st.top + prev_mini = 2 * mini
          prev_mini = (2 * mini) - st.top
          prev_mini = (2 * -3) - (-4) = -6 + 4
                    = -2
          stack = [-2, 0], mini = -2

=>  Intuition for why modified value in stack always < mini
          val < mini ( Ex. -3 < -2 )
          val - mini < 0
          -> adding val on both sides...
          val + val - mini < val
          (2 * val) - mini < val
          Here, the formula on L.H.S is indeed the modified value
          and from this we can say that... modified val < mini

"""
class MinStack:

    def __init__(self):
        self.stk = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(val)
            self.mini = val
        elif val > self.mini:
            self.stk.append(val)
        else:
            modified_val = (2 * val) - self.mini  # ---- (1)
            self.mini = val
            self.stk.append(modified_val)

    def pop(self) -> None:
        if self.stk[-1] > self.mini:
            # Just pop
            self.stk.pop()
        else:
            # It's modified value indeed
            # Need to rollback mini to previous mini
            # The formula to find previous mini comes from formula (1)
            prev_mini = (2*self.mini) - self.stk.pop()
            self.mini = prev_mini

    def top(self) -> int:
        if self.stk[-1] > self.mini:
            return self.stk[-1]
        else:
            # st.top is modified...so, we need to return original val.
            # original val. in that case is nothing but our self.mini
            return self.mini

    def getMin(self) -> int:
        return self.mini



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(2)
obj.pop()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
