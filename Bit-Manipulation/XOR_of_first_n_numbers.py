# Approach-1: O(N) time complexity
def xor_of_first_n(n):
    xor = 0
    for num in range(1,n+1):
        xor ^= num
    return xor

if __name__ == "__main__":
    n = int(input("n: "))
    print(f'XOR of 1 to {n} numbers is: {xor_of_first_n(n)}')
