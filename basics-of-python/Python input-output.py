# Take space separated input of integers list:

arr = list(map(int, input("enter nums list: ").strip().split()))

# The input() function takes user input as a string.
# strip(): This method is used to remove leading and trailing whitespace characters (spaces, tabs, newlines, etc.) from a string. 
# If no argument is provided, it removes all whitespace characters. For example:

text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

# split(): This method is used to split a string into a list of substrings based on a specified delimiter. 
# If no delimiter is provided, it splits the string using whitespace characters as the default delimiter. For example:

text = "apple,banana,orange"
fruits_list = text.split(',')
print(fruits_list)  # Output: ['apple', 'banana', 'orange']
