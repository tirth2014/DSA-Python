# Wrong Solution I came up with

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        no_of_char = n*2
        ans = []
        option = ['(',')']
        def helper(i,arr):
            if i>1 or len(arr) >= no_of_char:
                if len(arr) == no_of_char:
                    ans.append(''.join(arr))
                return
            elif i>1 and len(arr) < no_of_char:
                i = 0
            #pick
            arr.append(option[i])
            helper(i,arr)
            arr.pop()
            #not pick
            helper(i+1,arr)
        helper(0,[])
        return ans
# For n=2, it generates: ['((((', '((()', '(())', '()))', '))))']

# Correct-1 
  
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def helper(s,leftCnt,rightCnt):
        if leftCnt == rightCnt == n:
            ans.append(s)
          
        if leftCnt < n:
            helper(s+'(', leftCnt+1, rightCnt)

        # We're allowed to add closing parentheses only if open parentheses count is greater than closed parentheses
        # for ex. if open = 1 and closed = 1. i.e '()' then we can't add closed parentheses i.e. '())' this will be invalid.
        if rightCnt < leftCnt:
            helper(s+')', leftCnt, rightCnt+1)

    helper('',0,0)
    return ans
      
# Time Complexity:
# 1. The function uses recursion to generate all valid combinations of parentheses pairs, and it explores all possible combinations.
# 2. For each position in the output string, we have two choices: either add a '(' or a ')'.
# 3. Since we generate a total of `n * 2` characters, and at each step, we have two choices, the total number of recursive calls will be 2^(n * 2).
# 4. Each recursive call takes constant time, as we are only appending characters to the string `s` and performing comparisons.
# 5. Therefore, the overall time complexity can be expressed as O(2^(n * 2)), which is exponential in terms of `n`.

# In summary, the time complexity of the `generateParenthesis` function is O(2^(n * 2)) (exponential in `n`), and the space complexity is O(n) (linear in `n`). The function's time complexity makes it inefficient for larger values of `n`.
