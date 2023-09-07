# XOR:
# 1 ^ 1 = 0
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1

# Using XOR all numbers in pairs will be cancelled out and single number will remain at last.

def find_single_number(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor


if __name__ == "__main__":
    ip = input("enter list of numbers: ")
    ip = ip.replace(',',' ')
    nums = list(map(int, ip.split()))
    print(f'Single number in list: {nums} is = {find_single_number(nums)}')
