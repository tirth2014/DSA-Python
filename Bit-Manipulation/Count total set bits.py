if __name__ == '__main__':

    def set_bits_in_binary(num,res=0):
        if num > 1:
            res = set_bits_in_binary(num >> 1,res)
        if num & 1:
            res += 1
        return res

    def countSetBits(N: int) -> int:
        for num in range(1, N + 1):
            print(num, end=': ')
            print(set_bits_in_binary(num), end=', ')

    N = int(input("N: "))
    countSetBits(N)

# Output
# N: 16
# 1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1, 9: 2, 10: 2, 11: 3, 12: 2, 13: 3, 14: 3, 15: 4, 16: 1,
