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
    ans = prime_factorization(n)
