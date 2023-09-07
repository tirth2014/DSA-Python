# Approach-1: O(N) time complexity
def xor_of_first_n(n):
    xor = 0
    for num in range(1,n+1):
        xor ^= num
    return xor

if __name__ == "__main__":
    n = int(input("n: "))
    print(f'XOR of 1 to {n} numbers is: {xor_of_first_n(n)}')

# Optimal solutions - O(1) - for these kind of problems find patterns.

# Approach:2
"""
=> Pattern:
1     <--  1,5,9,13,17,...   (num ^ 2 = num + 2) and (num % 2 = 1)
next  <--  2,6,10,14,18,...  (num ^ 2 = num - 2) and (num % 2 = 0)
0     <--  3,7,11,15,19,...  (num ^ 2 = num - 2) and (num % 2 = 1)
same  <--  4,8,12,16,20,...  (num ^ 2 = num + 2) and (num % 2 = 0)
"""
def xor_of_first_n(n):
    if n ^ 2 == n + 2:
        if n % 2 == 0: return n
        elif n % 2 == 1: return 1

    elif n ^ 2 == n - 2:
        if n % 2 == 0: return n+1
        elif n % 2 == 1: return 0


if __name__ == "__main__":
    n = int(input("n: "))
    print(f'XOR of 1 to {n} numbers is: {xor_of_first_n(n)}')



# Approach:3

def xor_of_first_n(n):
    # if n is multiple of 4
    if n % 4 == 0:
        return n

    # If n % 4 gives remainder 1
    if n % 4 == 1:
        return 1

    # If n%4 gives remainder 2
    if n % 4 == 2:
        return n + 1

    # If n%4 gives remainder 3
    return 0


if __name__ == "__main__":
    n = int(input("n: "))
    print(f'XOR of 1 to {n} numbers is: {xor_of_first_n(n)}')
