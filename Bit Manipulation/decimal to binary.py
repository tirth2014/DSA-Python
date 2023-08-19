def dec_to_bin(num):
    res = []
    while num:
        rem = num//2
        res.append(str(num - (rem*2)))
        num = rem
    print("".join(res[::-1]))

num = int(input("Enter num: "))
dec_to_bin(num)

# Recursive Solution:

def dec_to_bin(num):                                 
    if num:
        dec_to_bin(num//2)
    print(num % 2,end="")

num = int(input("Enter num: "))
dec_to_bin(num)
# Ex. num = 10, res = 01010

d2b(11)
 |
 +-- d2b(5)
 |   |
 |   +-- d2b(2)
 |   |   |
 |   |   +-- d2b(1)
 |   |   |   |
 |   |   |   +-- d2b(0)
 |   |   |   |   |
 |   |   |   |   +-- Print 0
 |   |   |   +----Print 1
 |   |   +-- Print 0
 |   |
 |   +-- Print 1
 |
 +-- Print 1



# In-build format method:
def dec_to_bin(num):
    print(format(num,'b'))

num = int(input("Enter num: "))
dec_to_bin(num)   


The available integer presentation types are:

   +-----------+------------------------------------------------------------+
   | Type      | Meaning                                                    |
   |===========|============================================================|
   | "'b'"     | Binary format. Outputs the number in base 2.               |
   +-----------+------------------------------------------------------------+
   | "'c'"     | Character. Converts the integer to the corresponding       |
   |           | unicode character before printing.                         |
   +-----------+------------------------------------------------------------+
   | "'d'"     | Decimal Integer. Outputs the number in base 10.            |
   +-----------+------------------------------------------------------------+
   | "'o'"     | Octal format. Outputs the number in base 8.                |
   +-----------+------------------------------------------------------------+
   | "'x'"     | Hex format. Outputs the number in base 16, using lower-    |
   |           | case letters for the digits above 9.                       |
   +-----------+------------------------------------------------------------+
   | "'X'"     | Hex format. Outputs the number in base 16, using upper-    |
   |           | case letters for the digits above 9. In case "'#'" is      |
   |           | specified, the prefix "'0x'" will be upper-cased to "'0X'" |
   |           | as well.                                                   |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Number. This is the same as "'d'", except that it uses the |
   |           | current locale setting to insert the appropriate number    |
   |           | separator characters.                                      |
   +-----------+------------------------------------------------------------+
   | None      | The same as "'d'".                                         |
   +-----------+------------------------------------------------------------+
