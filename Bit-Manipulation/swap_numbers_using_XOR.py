# Approach:1 - With support of an extra variable
def swap_numbers(a,b):
    print(f'bfr func a  {id(a)}')
    print(f'bfr func b  {id(b)}')
    
    ab_xor = a ^ b    # ab_xor = 5 ^ 7 = 2
    a ^= ab_xor       # a = 5 ^ 2 = 7
    b ^= ab_xor       # b = 7 ^ 2 = 5
    
    print(f'aftr func a  {id(a)}')
    print(f'aftr func b  {id(b)}')
    return a,b

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    print(f'main a  {id(a)}')
    print(f'main b  {id(b)}')
    print(f'\n before swap: a = {a}, b = {b} \n')
    a,b = swap_numbers(a,b)
    print(f'\n after swap: a = {a}, b = {b} \n')
    print(f'aftr swap a  {id(a)}')
    print(f'aftr swap b  {id(b)}')

# Output console
# a: 5
# b: 7
# main a  9449888
# main b  9449952

#  before swap: a = 5, b = 7 

# bfr func a  9449888
# bfr func b  9449952
# swap func a  9449952
# swap func b  9449888

#  after swap: a = 7, b = 5 

# aftr swap a  9449952
# aftr swap b  9449888

# Python’s argument passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 



# Approach:2 - without using any other variable
def swap_numbers(a,b):
    print(f'bfr func a  {id(a)}')
    print(f'bfr func b  {id(b)}')

    a = a ^ b   # a = 5 ^ 7
    b = b ^ a   # b = 7 ^ 5 ^ 7 = 5 (as two 7's will cancel out each other)
    a = a ^ b   # a = 5 ^ 7 ^ 5 = 7 (as two 5's will cancel out each other)

    return a,b

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    print(f'\n before swap: a = {a}, b = {b} \n')
    a,b = swap_numbers(a,b)
    print(f'\n after swap: a = {a}, b = {b} \n')
