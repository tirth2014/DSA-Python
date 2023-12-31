def kDistinctChars(k, s):
    # Return an integer value
    n, dict = len(s), {}
    i = j = res = 0
    while j < n:
        dict[s[j]] = dict.get(s[j], 0) + 1        
        while len(dict) > k:
            dict[s[i]] -= 1
            if dict[s[i]] == 0:
                del dict[s[i]]
            i += 1
        j += 1
        res = max(res, j - i)
    return res
