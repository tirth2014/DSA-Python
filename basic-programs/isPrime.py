# Naive approach
def isPrime(n: int) -> bool:
    if n in [0,1]: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



 # efficient:
def isPrime(n: int) -> bool:
    if n in [0,1]: return False
      
    sqrt_n = int(n ** (1/2))  # or int(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if n % i == 0:
            return False
    return True



# Most efficient
if __name__ == '__main__':
  
    def isPrime(n: int) -> bool:
        if n in [0,1]: return False
        elif n in [2,3]: return True
        elif n % 2 == 0 or n % 3 == 0: return False
          
        sqrt_n = int(n ** (1/2))  # or int(math.sqrt(n))
        for i in range(5, sqrt_n+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True

    n = int(input("n: "))
    ans = isPrime(n)
    print("ans: ", ans)
