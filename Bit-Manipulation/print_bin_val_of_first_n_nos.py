# Using division and modulo operators
if __name__ == '__main__':

    def print_binary(num):
        if num > 1:
            print_binary(num//2)
        print(num % 2, end=" ")


    N = int(input("enter N: "))
    for i in range(1,N+1):
        print(i, end=': ')
        print_binary(i)
        print()


# Using bitwise operators (recursively)
if __name__ == '__main__':
    def print_binary(num):
        if num > 1:
            # Right shift by 1 position means divide by 2
            # 6 = 110, 6 >> 1 = 11 = 3
            print_binary(num >> 1)
        # odd => 1 and even => 0
        print(num & 1, end=" ")

    N = int(input("enter N: "))
    for i in range(1,N+1):
        print(i, end=': ')
        print_binary(i)
        print()

# Output Console
# enter N: 5
# 1: 1 
# 2: 1 0 
# 3: 1 1 
# 4: 1 0 0 
# 5: 1 0 1


# Iterative
def print_binary(num):
    bin_n = ''
    while num:
        bin_n = str(num & 1) + bin_n
        num = num >> 1
    return bin_n

N = int(input("enter N: "))
for i in range(1,N+1):
    print(i, end=': ')
    print(print_binary(i))
