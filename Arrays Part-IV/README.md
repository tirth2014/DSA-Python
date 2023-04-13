Arrays Part-IV
This repository contains Python implementations of some array-based problems from LeetCode.

Table of Contents
Two Sum
3Sum
Best Time to Buy and Sell Stock
Maximum Subarray
Product of Array Except Self
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Link to Solution: two_sum.py

3Sum
Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.

Link to Solution: three_sum.py

Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Link to Solution: buy_sell_stock.py

Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Link to Solution: maximum_subarray.py

Product of Array Except Self
Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

**




Tirth Patel
i want full description (i.e with example testcases) 

2 / 2

Arrays Part-IV
This repository contains Python implementations of some array-based problems from LeetCode.

Table of Contents
Two Sum
3Sum
Best Time to Buy and Sell Stock
Maximum Subarray
Product of Array Except Self
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [




Tirth Patel
continue
3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Link to Solution: two_sum.py

3Sum
Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.

Note that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Link to Solution: three_sum.py

Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Link to Solution: buy_sell_stock.py

Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Link to Solution: maximum_subarray.py

Product of Array Except Self
Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3




Tirth Patel
continue
]
Output: [0,0,9,0,0]

Link to Solution: product_except_self.py

Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [1,1]
Output: 1

Example 4:

Input: nums = [1,1,2]
Output: 1

Link to Solution: find_duplicate_number.py

Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Link to Solution: spiral_matrix.py

Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

rotate_image_1

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

rotate_image_2

Input: matrix = [[1]]
Output: [[1]]

Link to Solution: rotate_image.py
