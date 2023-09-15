# T.C: O(n) worst case
# Worst Case: When "n" is a prime number...outer for loop runs till n
# Not O(n^2) because the inner while loop reduces "n" everytime
if __name__ == '__main__':
    def prime_factorization(n):
        for i in range(2,n):
            while n % i == 0:
                print(i,end=' ')
                n /= i
    
    n = int(input("n: "))
    prime_factorization(n)

# output console:
# n: 48
# 2 2 2 2 3 


# A little optimized:
# T.C: O(sqrt(n)) worst case
if __name__ == '__main__':
    # Every no. has prime factorization apart from no. itself that's <= sqrt(n)
    # Using this property to optimize
    def prime_factorization(n):
        for i in range(2,int(n**0.5)+1):
            while n % i == 0:
                print(i,end=' ')
                n /= i
        if n > 1:
            print(int(n), end=' ')

    n = int(input("n: "))
    prime_factorization(n)


# A maximum no. of prime factors a number can have = log2(n)...as 2 is the smallest prime factor for any number.
# Using this property and Sieve of Eratosthenes...we'll maintain a sieve or spf array (smallest prime factor array)
# All the numbers in the spf array will have their smallest prime factor...and for prime numbers the number itself.
# It's the most efficient method to find prime factors of any given number for even larger testcases
# Worst Case T.C:  O(log2(n)) i.e. log(n) base 2 

if __name__ == '__main__':
    def prime_factorization(n):
        # Initialize sieve or spf array of size n+1 with the numbers itself
        spf = [i for i in range(n+1)]

        # Using the concept that smallest prime factor for "n" is <= sqrt(n)
        for i in range(2, int(n**0.5)+1):
            if spf[i] == i:
                # Mark the smallest factor as "i" for all multiples of "i" in the spf array
                for j in range(i*i,n+1,i):
                    if spf[j] == j:  # If a number is itself and doesn't already have the smallest prime factor stored.
                        spf[j] = i

        # Our sieve (spf array) is ready to use now with O(1) lookup.
        num = n
        while num != 1:
            print(spf[num],end=' ')
            num //= spf[num]

    n = int(input("n: "))
    prime_factorization(n)
