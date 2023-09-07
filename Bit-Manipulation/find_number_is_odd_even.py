# This is slower way to check if no. is odd or even
def slow_odd_even_finder(num):
  if num % 2 == 0:
    return "even"
  else:
    return "odd"

num = int(input("enter a number: "))
print(slow_odd_even_finder(num))


# Fastest way (Using bit manipulation):
# '&' operator use-case
# As in odd numbers 2^0 = 1 bit will always be set so we can utilize this property.
def fastest_odd_even_finder(num):
  if num & 1 == 0:
    return "even"
  else:
    return "odd"

num = int(input("enter a number: "))
print(fastest_odd_even_finder(num))
