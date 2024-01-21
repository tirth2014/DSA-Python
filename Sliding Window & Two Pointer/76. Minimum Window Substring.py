# First Accepted solution with kharaab time complexity:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = {}
        for char in t:
            if char not in t_counter:
                t_counter[char] = 1
            else:
                t_counter[char] += 1

        i = j = 0
        n = len(s)
        min_len = (2**31)-1
        res = ''
        while j < n:
            if s[j] in t_counter:
                t_counter[s[j]] -= 1
            while all(val <= 0 for val in t_counter.values()):
                curr_len = j-i+1
                if curr_len < min_len:
                    min_len = curr_len
                    res = s[i:j+1]

                if s[i] in t_counter:
                    t_counter[s[i]] += 1
                i += 1
            j += 1

        while i < j:
            if all(val <= 0 for val in t_counter.values()):
                curr_len = j-i+1
                if curr_len < min_len:
                    min_len = curr_len
                    res = s[i:j+1]

            if s[i] in t_counter:
                t_counter[s[i]] += 1
            i += 1

        return res
      


# Optimal Solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        m == s.length
        n == t.length
        1 <= m, n <= 105
        Time Complexity: O(m+n)
        """
        t_counter = {}

        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        i = j = 0
        n = len(s)
        min_len = float('inf')
        res = ''
        # Directly check using this single int. variable
        # No need to check for all characters individually in t_counter if they're < 0
        # and increase time complexity needlessly
        required_chars_len = len(t)

        while j < n:
            if s[j] in t_counter:
                # Imp. case: s = bba, t = ab
                # In this case, when b appears second time then it's necessary to decrease it further
                # in t_counter to -1, otherwise in while loop below it'll be increased to 1 from 0
                # and ans will be "bba" instead of correct ans. "ba"
                if t_counter[s[j]] > 0:
                    required_chars_len -= 1
                t_counter[s[j]] -= 1  # Decrease even if it's 0 already.

            while required_chars_len == 0:
                curr_len = j-i+1
                if curr_len < min_len:
                    min_len = curr_len
                    res = s[i:j+1]

                if s[i] in t_counter:
                    t_counter[s[i]] += 1
                    # Imp. condition again
                    # In case, s = bba, t = ab when increasing i from 0 to 1
                    # then, t_counter = {a: 0, b: -1}, so, t_counter[s[i]] += 1 will make
                    # t_counter = {a: 0, b: 0}, In this case, "required_chars_len" shouldn't be incremented.
                    if t_counter[s[i]] > 0:
                        required_chars_len += 1
                i += 1
            j += 1
        return res

if __name__ == '__main__':
    ob = Solution()
    for t in range(int(input("#testcases: "))):
        # arr = list(map(int, input("arr: ").split()))
        # arr = ast.literal_eval(input("arr: "))
        st1 = input("s: ")
        st2 = input("k: ")
        # k = int(input("k: "))
        # num = input("num string: ")
        ans = ob.minWindow(st1,st2)
