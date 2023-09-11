"""
Set the rightmost unset bit. Return same number if all bits are set.
Ex:
10 -> 1010
output -> 1011
https://www.codingninjas.com/studio/problems/set-the-rightmost-unset-bit_8160456
"""

from typing import *

if __name__ == '__main__':
    def setBits(N: int) -> int:
        if N ^ N+1 == (N << 1)+1:
            return N

        return N | N+1

    N = int(input("N: "))
    res = setBits(N)
    print(f"{N}: {bin(N).replace('0b','')}")
    print(f"{res}: {bin(res).replace('0b','')}")


# Output console:
# N: 8
# 8: 1000
# 9: 1001

# N: 15
# 15: 1111
# 15: 1111
