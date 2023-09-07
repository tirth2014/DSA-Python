"""
Problem:    Given a range L,R
Returns:    XOR of (L ^ L+1 ^ L+2 ^,....^ R-1 ^ R)
"""

# Brute-force solution - O(N):
def xor_range_lr(L, R):
    # XOR of range(L,R) = (XOR of first L-1 numbers) ^ (XOR of first R numbers)
    xor = 0
    for num in range(L,R+1):
        xor ^= num
    return xor


if __name__ == "__main__":
    l = int(input("L: "))
    r = int(input("R: "))
    print(f'XOR of range {l, r} is: {xor_range_lr(l, r)}')




# Optimal solution - O(1)
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


def xor_range_lr(L, R):
    # XOR of range(L,R) = (XOR of first L-1 numbers) ^ (XOR of first R numbers)
    return xor_of_first_n(L - 1) ^ xor_of_first_n(R)


if __name__ == "__main__":
    l = int(input("L: "))
    r = int(input("R: "))
    print(f'XOR of range {l, r} is: {xor_range_lr(l, r)}')
