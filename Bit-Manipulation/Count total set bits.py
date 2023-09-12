# Count #1's or set-bits, Also known as "Hamming Weight"

if __name__ == '__main__':

    def set_bits_in_binary(num,res=0):
        if num > 1:
            res = set_bits_in_binary(num >> 1,res)  # Right-shift the num by 1
        if num & 1:
            res += 1
        return res

    def countSetBits(N: int) -> int:
        for num in range(1, N + 1):
            print(f"{num}({bin(num).replace('0b','')})", end=': ')
            print(set_bits_in_binary(num), end=', ')

    N = int(input("N: "))
    countSetBits(N)

# Output
# N: 16
# 1(1): 1, 2(10): 1, 3(11): 2, 4(100): 1, 5(101): 2, 6(110): 2, 7(111): 3, 8(1000): 1, 9(1001): 2, 10(1010): 2, 11(1011): 3, 12(1100): 2, 13(1101): 3, 14(1110): 3, 15(1111): 4, 16(10000): 1, 



# Approach-2:
# put counter and keep removing rightmost 1 till "num" becomes 0
if __name__ == '__main__':
    
    def set_bits_in_binary(num):
        res = 0
        while num:
            res += 1
            num &= num-1  # Removes right-most set-bit(1) from num
        return res

    def countSetBits(N: int) -> int:
        for num in range(1, N + 1):
            print(f"{num}({bin(num).replace('0b','')})", end=': ')
            print(set_bits_in_binary(num), end=', ')

    N = int(input("N: "))
    countSetBits(N)
