def check_i_th_bit_set(num,i):
    # Using left-shift operator to get mask
    mask = 1 << i       # left shift 1 by i places.
    print(f"mask: {bin(mask).replace('0b','')}")
    return num & mask


num = int(input("enter a number: "))
i = int(input("enter i: "))
print(f"num {num}: {bin(num).replace('0b','')}")
is_set = check_i_th_bit_set(num,i)
print(f"bit #{i} in {num} is: {'Set' if is_set else 'Not Set'}")

# Output console:
# enter a number: 10
# enter i: 3
# num 10: 1010
# mask: 1000
# bit #3 in 10 is: Set
