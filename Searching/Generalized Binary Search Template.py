# Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascend order. For most tasks, we can transform the requirement into the following generalized form:

# Minimize k , s.t. condition(k) is True

# The following code is the most generalized binary search template:
  
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
  
# What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

# Correctly initialize the boundary variables left and right. Only one rule: set up the boundary to include all possible elements;
# Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
# Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
  
