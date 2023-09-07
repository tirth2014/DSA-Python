def set_i_th_bit(num,i):
    mask = 1 << i       # left shift 1 by i places.
    print(f"mask: {bin(mask).replace('0b','')}")
    return num | mask


num = int(input("enter a number: "))
i = int(input("enter i: "))
print(f"num {num}: {bin(num).replace('0b','')}")
res = set_i_th_bit(num,i)
print(f"after set num is {res}: {bin(res).replace('0b','')}")
