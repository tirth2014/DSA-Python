def print_names(i=0):
    if i == 5:   # BASE CASE
        return
    print('Tirth')
    print_names(i+1)

print_names()


# RECURSION TREE:

print_names(0)
-> print_names(1)
    -> print_names(2)
        -> print_names(3)
            -> print_names(4)
                -> print_names(5)
                -> return
            -> return
        -> return
    -> return
-> return


"""
Each call to print_names creates a new stack frame (or node in the tree), with the current value of i passed as an argument. 
The tree continues to grow until i reaches 5, at which point the function returns and the tree starts to collapse from the bottom up. 
The return values are propagated back up the tree until the original call to print_names returns and the program terminates.
the base case will be triggered after 5 recursive calls.
"""
