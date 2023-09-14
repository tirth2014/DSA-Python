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
