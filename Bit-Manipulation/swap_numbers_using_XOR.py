def swap_numbers(a,b):
    print(f'bfr func a  {id(a)}')
    print(f'bfr func b  {id(b)}')
    
    ab_xor = a ^ b
    a ^= ab_xor
    b ^= ab_xor
    
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
