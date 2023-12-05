
"""
Problem: We're given an array and an integer s, representing the subarray size. We've to find the maximum sum from all
subarrays of size s.

Ex:
Input:
A : [2,3,5,2,9,1]
s = 2

Solution:
-> All 2 size subarrays with their sum:
[2,3] = 5
[3,5] = 8
[5,2] = 7
[2,9] = 11
[9,1] = 10

ans: 11

"""
# Brute Force (Noob approach)
import sys
import ast

def find_max_sum(arr, s):
    n = len(arr)
    curr_max = -sys.maxsize - 1
    for i in range(n):
        curr_sum = 0
        if i <= (n - i + 1):
            for j in range(i, i+s):
                curr_sum += arr[j]
            if curr_sum > curr_max:
                curr_max = curr_sum
    return curr_max


if __name__ == "__main__":

    A = ast.literal_eval(input("Enter array: "))
    s = int(input("Enter subarray size: "))

    res = find_max_sum(A,s)
    print(res)


# Can we improve?
# How to identify?

# 1. Repeatative Work then definitely we can optimize:
# Yes, here we're repeating same numbers in all window except adding 1 new.
# Ex: [2,3,1,5,6,7,8]
# s = 3
# [2,3,1], [3,1,5], [1,5,6], [5,6,7], [6,7,8]....here last 2 digits from previous window are repeating in next window as well, only first digit changed with a new digit.
