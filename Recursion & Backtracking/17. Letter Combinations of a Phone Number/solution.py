# My backtracking solution ( Fails for len(digits) > 2)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping is right...we can do it directly too or using string library of python too.
        if not digits:
            return []

        small = list(map(chr, range(ord('a'), ord('z')+1)))
        mapping = {}
        ptr = 0
        for i in range(2,10):
            if i == 7 or i == 9:
                mapping[str(i)] = small[ptr:ptr+4]
                ptr = ptr+4
            else:
                mapping[str(i)] = small[ptr:ptr+3]
                ptr = ptr+3

        digits_str_lst = [''.join(lst) for lst in [mapping[ch] for ch in digits]]
        res = []
      
        # -- ACTUAL LOGIC --
        if len(digits) > 1:
            def helper(comb):
                if len(comb) == len(digits):
                    res.append(comb)
                    return
                if len(comb) > len(digits):
                    return
                for l_ptr1,st1 in enumerate(digits_str_lst):
                    for ch1 in st1:
                        for st2 in digits_str_lst[l_ptr1+1:]:
                            for ch2 in st2:
                                helper(comb+ch1+ch2)
        else:
            def helper(comb):
                nonlocal res
                res = [*digits_str_lst[0]]

        helper("")
        return res


# Backtracking solution
# Beats 99.57%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        if len(digits) ==0:
            return res
            
        def dfs(index=0,path=""):
            # Using "index" is the key thing here in recursive solution.
            if index >= len(digits):
                res.append(path)
                return

            string1 = mapping[digits[index]]
            for ch in string1:
                dfs(index+1, path+ch)

        dfs()
        return res
