# Parameterised and Functional Recursion

# Parameterised

def print_sum(i,sum=0):
  if i < 1:
    print(sum)
    return
  print_sum(i-1,sum+i)

print_sum(4)  # 10



# Functional

def print_sum(n):
  if n==0:
    return 0
  return n + print_sum(n-1)

print(print_sum(4))# 10
