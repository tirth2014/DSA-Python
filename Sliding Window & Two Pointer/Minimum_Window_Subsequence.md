[ Minimum Window Subsequence](https://www.codingninjas.com/studio/problems/minimum-window-subsequence_2181133?leftPanelTabValue=PROBLEM "@embed")

### Problem statement
You are given two strings `S` and `T`. Your task is to find the minimum (Contiguous) substring `W` of `S`, such that `T` is a subsequence of `W`

A subsequence is a sequence that can be derived from another sequence by removing zero or more elements, without changing the order.

A substring is a contiguous part of a string.

For example:
For the given string `CodingNinjas`: `Ninja` is a substring while `inas` is a subsequence. 
If there is no such Window in `S` that covers all characters in `T`, return an empty string "". If there are multiple such minimum length windows, return the one with the smallest starting index.

### Solution

 - If `j` is at the beginning of `T`, update `start` to the current index `i`.
 
 - If `j` is at the end of `T`, calculate the length of the current window `(i - start + 1)` and check if it's shorter than the current minimum window length `ans_len`. If it is, update `ans_len` and `ans` accordingly.
 
 - Increment `j` using modular arithmetic to ensure it wraps around if it reaches the end of `T`.

```python Python
# Worst case T.C: O(len(str1) * len(str2)) and if both strings of same length that's O(N^2)

class Solution:

    @staticmethod
    def minWindow(S, T):
        i = j = start = 0
        s_len, t_len, ans_len = len(S), len(T), float('inf')
        ans = ""
        while i < s_len:
            if S[i] == T[j]:
                if j == 0:
                    start = i
                if j == t_len - 1 and i - start + 1 < ans_len:
                    ans_len = i - start + 1
                    ans = S[start: i+1]
                    i = start
                j = (j + 1) % t_len
            i += 1
        return ans


if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        st1 = input("s: ")
        st2 = input("k: ")
        ans = ob.minWindow(st1, st2)
        print(ans)

```
 
