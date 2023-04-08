s = "madam"
def check_palindrome(i=0):
  n = len(s)
  if i >= n//2: return True     # BASE CASE
  if s[i] != s[n-i-1]: return False
  return check_palindrome(i+1)   # Don't forget return statement here otherwise it'll return None

res = check_palindrome()
print(res)
