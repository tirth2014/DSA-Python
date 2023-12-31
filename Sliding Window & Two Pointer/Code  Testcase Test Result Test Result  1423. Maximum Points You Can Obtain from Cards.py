"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
"""

# The main idea:  Understand how sliding window is applied
# Sliding window on remaining elements window ( window size: n-k ) and not on elements to be considered in k

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        i, j = 0, n-k   # window size = (n-k)
        if j == 0:  # If k == n
            return sum(cardPoints)
        max_sum = curr_sum = sum(cardPoints[j:])
        while j < n:
            curr_sum += (cardPoints[i] - cardPoints[j])
            max_sum = max(max_sum, curr_sum)
            j += 1
            i += 1
        return max_sum
