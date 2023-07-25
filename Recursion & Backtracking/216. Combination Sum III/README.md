## <a href='https://leetcode.com/problems/combination-sum-iii/description'> 216. Combination Sum III </a>
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Likes](https://img.shields.io/badge/Likes-5.2k-green)
![Recursion](https://img.shields.io/badge/Tag-Recursion-blue)
![Backtracking](https://img.shields.io/badge/Tag-Backtracking-yellow)

### Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

Only numbers `1` through `9` are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

### Example 1:
<pre><strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

### Example 2:
<pre><strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

### Example 3:
<pre><strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 <br/>and since 10 &gt; 1, there are no valid combination.
</pre>
 

# Constraints:

`2 <= k <= 9`
`1 <= n <= 60`

## Statistics
![Accepted](https://img.shields.io/badge/Accepted-418.5K-brightgreen)
![Submissions](https://img.shields.io/badge/Submissions-614.2K-blue)
![Acceptance Rate](https://img.shields.io/badge/Acceptance%20Rate-68.1%25-yellow)
