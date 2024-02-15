"""
Three way partitioning

https://www.geeksforgeeks.org/problems/three-way-partitioning/1

Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Note: The generated output is 1 if you modify the given array successfully.
"""

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    i, start, end = 0, 0, len(array)-1
	    
	    while i <= end:
	        if array[i] < a:
	            array[i], array[start] = array[start], array[i]
	            i += 1
	            start += 1
	           
	        elif array[i] >= a and array[i] <= b:
	            i += 1
	           
	        elif array[i] > b:
                array[i], array[end] = array[end], array[i]
                end -= 1
        
        return array
