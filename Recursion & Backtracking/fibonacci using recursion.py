def fib(n):
  if n <= 1: return n
  return fib(n-1) + fib(n-2)


if __name__ == "__main__":
  print(fib(4)) # 3

  # Fibonacci series: 1,1,2,3,5,8,13....

