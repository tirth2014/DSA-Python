def recursive_fun():
  
  BASE CASE
  condition satisfied => return 1
  condition not satisfied => return 0
  
  # If there are 2 recursive calls
  l = fun()
  r = fun()
  
  return l+r


  # else if there are "n" recursive calls [ This pattern is used in N-Queens problem]
  s = 0
  recursive_fun(i = 1 -> n)
    s += recursive_fun()
  return s
  

# This pattern is also imp. in dynamic programming
  
