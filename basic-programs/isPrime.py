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



# Further optimization
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




"""
Sieve of Eratosthenes
You can call this function with a value of N, and it will return a list of all prime numbers up to N.
The Sieve of Eratosthenes is efficient for finding primes in a large range and has a time complexity of O(N*log(log N)), making it one of the fastest prime-generating algorithms available.

1. Initialize: 
   Create a list of Boolean values (True or False) for each integer from 2 to the given limit N. Initially, set all values to True, indicating that they are potential prime numbers.

2. Start with the first prime, 2: 
   2 is the smallest prime number. Mark all multiples of 2 as not prime (False) since they are divisible by 2 but no other prime number smaller than 2.

3. Find the next prime: 
   Starting from 2, search for the next True value in the list. This value is the next prime number.

4. Mark multiples of the prime as not prime: 
   Once you find a prime number, say p, mark all multiples of p (greater than p) in the list as False since they are divisible by p.

5. Repeat steps 3 and 4: 
   Continue this process until you have checked all numbers up to the square root of N. At this point, all remaining True values in the list correspond to prime numbers.

6. Retrieve the prime numbers: 
   After the algorithm finishes, the indices of the True values in the list represent the prime numbers within the range of 2 to N.
"""
def createSieve(N):
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
    return sieve

def isPrime(n: int) -> bool:
    sieve = createSieve(n)
    return sieve[n]
