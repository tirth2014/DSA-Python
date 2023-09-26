"""
Start with an empty stack.
Push all the people onto the stack.

While there are at least two people on the stack, do the following:
Pop the top two people (A and B) from the stack.
Check if A knows B:
If A knows B, then A cannot be a celebrity, so discard A.
If A does not know B, then B cannot be a celebrity, so discard B.
Continue this process until only one person remains on the stack.
The remaining person on the stack is a potential celebrity candidate.

To verify if the candidate is indeed a celebrity, iterate through all the people and check two conditions:
1. The candidate does not know anyone.
2. Everyone else knows the candidate. 
"""

from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):
    stack = list(range(n))
    
    while stack and len(stack) > 1:
        p1 = stack.pop()
        p2 = stack.pop()
        if knows(p1,p2) and not knows(p2, p1):
            stack.append(p2)
        elif knows(p2,p1) and not knows(p1, p2):
            stack.append(p1)
    
    if stack:
        for person in range(n):
            if person == stack[-1] or knows(person, stack[-1]):
                continue
            else:
                return -1
    return stack[-1] if stack else -1


    

            
