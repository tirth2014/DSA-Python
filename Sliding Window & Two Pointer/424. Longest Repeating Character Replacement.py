# 1. Sliding Window Technique:
# The solution employs a sliding window approach with two pointers, i and j, representing the left and right ends of the current window.

# 2. Maintaining a Character Count Dictionary:
# The cnt_dict dictionary is used to keep track of the count of characters in the current window.

# 3. Expanding the Window:
# Initially, the window starts with both pointers at the beginning of the string. As the right pointer (j) moves, the count of the encountered characters is updated in the cnt_dict.

# 4. Checking Validity of the Window:
# At each step, the code checks whether the window can be made valid by replacing at most k characters. This is determined by calculating the length of the window (window_len) minus the count of the most frequently occurring character in the window. If this value is less than or equal to k, the window is considered valid.

# 5. Updating the Result:
# If the window is valid, the maximum length encountered so far (res) is updated.

# 6. Contracting the Window:
# If the window is not valid, the left pointer (i) is moved one step to the right, and the count of the character at that position is reduced. This process continues until a valid window is obtained.

# 7. Iterating through the String:
# The process continues until the right pointer (j) reaches the end of the string.

# 8. Final Result:
# The function returns the maximum length of a valid substring obtained during the iterations.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res, i, j = 0, 0, 0
        cnt_dict = {}
        while j < n:
            window_len = j-i+1
            cnt_dict[s[j]] = cnt_dict.get(s[j], 0) + 1
            if window_len - max(cnt_dict.values()) <= k:
                res = max(res, window_len)
            else:
                cnt_dict[s[i]] = cnt_dict.get(s[i], 0) - 1
                i += 1
            j += 1
        return res



# A slight optimization by using "max_freq" variable instead of looking everytime for max. count from dictionary which takes O(26*N)...we reduced to O(N)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res, max_freq, i, j = 0, 0, 0, 0
        cnt_dict = {}
        while j < n:
            window_len = j-i+1
            cnt_dict[s[j]] = cnt_dict.get(s[j], 0) + 1
            max_freq = max(max_freq, cnt_dict[s[j]])
            if window_len - max_freq <= k:
                res = max(res, window_len)
            else:
                cnt_dict[s[i]] = cnt_dict.get(s[i], 0) - 1
                i += 1
            j += 1
        return res
