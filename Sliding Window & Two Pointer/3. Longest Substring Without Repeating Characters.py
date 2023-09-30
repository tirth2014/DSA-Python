# Brute force approach
# Time Complexity: O(N^2)
# Space Complexity: O(N) where N is the size of HashSet taken for storing the elements
class Solution:
    def lengthOfLongestSubstring(self, ip_str: str) -> int:
        if len(ip_str) == 0:
            return 0
        res = 0
        for i in range(len(ip_str)):  # outer loop for traversing the string
            seen_set = set()
            # nested loop for getting different string starting with ip_str[i]
            for j in range(i, len(ip_str)):
                if ip_str[j] in seen_set:  # if element is already seen, break from the inner loop.                
                    break
                seen_set.add(ip_str[j])
                res = max(res, j-i+1)
        return res


# Optimized - 1:
# set + 2-ptr  approach
# Time:   O(2*N) 
# Space: O(N)
class Solution:
    def lengthOfLongestSubstring(self, ip_str: str) -> int:
        seen_set = set()
        res = 0
        lI = 0
        for rI in range(len(ip_str)):
            if ip_str[rI] in seen_set:
                # This means current window has somewhere repeating character
                # keep moving "lI" by one step and removing elements from set
                # till the repeated one is removed
                while ip_str[rI] in seen_set:
                    seen_set.remove(ip_str[lI])
                    lI += 1
            res = max(res, (rI-lI+1))
            seen_set.add(ip_str[rI])
        return res


# Optimal:
# HashMap + 2-ptr approach
# T.C : O(N)
# S.C:  O(N)
class Solution:
    def lengthOfLongestSubstring(self, ip_str: str) -> int:
        seen_map = {}
        res = 0
        lI = 0
        for rI in range(len(ip_str)):
            if ip_str[rI] in seen_map and seen_map[ip_str[rI]] >= lI:
                # old approach -------  O(2*N)
                # This means current window has somewhere repeating character
                # keep moving lI by one step and removing elements from set
                # till the repeated one is removed
                # ---- new approach ---  O(N)
                # directly jump to the next of repeating char. by leveraging index
                # stored in seen_map. No need to remove elements one by one just
                lI = seen_map[ip_str[rI]] + 1
            res = max(res, (rI-lI+1))
            seen_map[ip_str[rI]] = rI
        return res
