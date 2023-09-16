"""
Prefix to Infix
https://www.geeksforgeeks.org/prefix-infix-conversion/

Algorithm for Prefix to Infix:

-> Read the Prefix expression in reverse order (from right to left)
-> If the symbol is an operand, then push it onto the Stack
-> If the symbol is an operator, then pop two operands from the Stack
-> Create a string by concatenating the two operands and the operator between them.
   string = (operand1 + operator + operand2)
   And push the resultant string back to Stack
-> Repeat the above steps until the end of Prefix expression.

At the end stack will have only 1 string i.e resultant string
"""

def prefixToinfix(prefix_expr: str) -> str:
    stack = []
    infix_expr = ""

    for ch in prefix_expr[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            # ch is operator
            st = f"({stack.pop()}{ch}{stack.pop()})"
            # OR st = '(' + stack.pop() + str(ch) + stack.pop() + ')'
            stack.append(st)
    while stack:
        infix_expr += stack.pop()

    return infix_expr


t = int(input("Enter #testcases: "))
while t:
    prefix_expression = input("prefix expression: ")
    infix_expr = prefixToinfix(prefix_expression)
    print('prefix_expression: ', prefix_expression)
    print('infix_expression: ', infix_expr)
    t -= 1


# Enter #testcases: 2

# prefix expression: *+AB-CD
# infix_expression:  ((A+B)*(C-D))

# prefix expression: *-A/BC-/AKL
# infix_expression:  ((A-(B/C))*((A/K)-L))
