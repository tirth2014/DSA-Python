# => RECURSION
# Recursion is a technique where a function calls itself with a simpler or smaller version of the problem 
# until a base case is reached. Recursion can be used to solve problems that can be broken down into smaller 
# sub-problems of the same type. The function calls itself repeatedly until the base case is reached, 
# at which point the solution is returned.

def print_1_to_n(i,n):
    if i > n:
        return
    print(i,end=" ")
    print_1_to_n(i+1,n)

print_1_to_n(1,10)


# => BACKTRACKING
# Backtracking is a systematic way of exploring all possible solutions to a problem 
# by generating a sequence of decisions, one at a time, and testing each decision against the constraints of the problem. 
# If a decision violates a constraint, the algorithm "backs up" to the previous decision point and tries a different option.

# Backtracking is commonly used in search problems, such as finding a path through a maze, 
# or finding a solution to a Sudoku puzzle, or generating all possible permutations of a set of elements. 
# The algorithm works by maintaining a state of the search process, and when a dead-end is reached, 
# the algorithm "backs up" to a previous state and tries a different path until a solution is found or all possibilities have been explored.

# => DIFFERENCE BETWEEN RECURSION AND BACKTRACKING:
# In essence, backtracking can be seen as a generalization of recursion, 
# where the function calls itself repeatedly, but also explores multiple options at each recursive call. 
# While recursion is useful for solving problems that can be broken down into smaller sub-problems, 
# backtracking is useful for exploring all possible solutions to a problem, 
# incrementally building up a solution, and abandoning those that violate the constraints of the problem.

def print_1_to_n_backtracking(i,n):
    if i < 1:
        return
    print_1_to_n_backtracking(i-1, n)
    print(i,end=" ")
    
print_1_to_n_backtracking(10,10)

