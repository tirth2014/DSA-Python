## Problem Statement: 
Add 2 integers without using +, -, *, / operators.

## Asked in:
[Zeus Learning](https://www.geeksforgeeks.org/zeus-learning-interview-experience-for-software-developer-on-campus/)


## Solution
Use Bit manipulation

```py
def add_without_arithmetic(a: int, b: int) -> int:
    while b != 0:
        carry = a & b  # Calculate the carry (common set bits of a and b)
        a = a ^ b      # Calculate the sum (bitwise XOR of a and b)
        b = carry << 1 # Shift the carry by one bit to the left to add it to the sum
    return a

# Test the function
print(add_without_arithmetic(5, 7))  # Output: 12
```

### Example:
a = 7, b= 5

</br>
 
a = 111,  b = 101 </br>

(1) carry = a & b   </br>
 carry =  111 & 101 = 101 (5) </br>
 a = 111 ^ 101 = 010 (2)  </br>
b =  101 (5) << 1 = 10 (1010) </br>

(2) carry = 2 & 5 = 0010 & 1010 = 10 (2) </br>
a = 2 ^ 10 = 0010 ^ 1010 = 1000 = 8  </br>
b = 2 << 1 = 10 << 1  = 4   </br>

(3) carry = 8 & 4 = 1000 & 0100 = 0 </br>
a = 8 ^ 4 = 1000 ^ 0100 = 1100 = 12 </br>
b = 0  </br>

### result = a = 12
