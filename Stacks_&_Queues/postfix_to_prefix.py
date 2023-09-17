"""
Algorithm for Postfix to Prefix:

1. Read the Postfix expression from left to right
2. If the symbol is an operand, then push it onto the Stack
3. If the symbol is an operator, then pop two operands from the Stack
4. Create a string by concatenating the two operands and the operator before them.
   string = operator + operand2 + operand1
   And push the resultant string back to Stack
5. Repeat the above steps 1-4 until the end of the Postfix expression.
"""


def postfixToPrefix(prefix_expr: str) -> str:
    stack = []
    for ch in prefix_expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            st = str(ch) + p2 + p1
            stack.append(st)
    if stack:
        return stack.pop()


t = int(input("Enter #testcases: "))
while t:
    postfix_expression = input("\npostfix expression: ")
    prefix_expression = postfixToPrefix(postfix_expression)
    print('postfix_expression: ', prefix_expression)
    t -= 1


# OUTPUT
# Enter #testcases: 2

# postfix expression: AB+CD-*
# postfix_expression:  *+AB-CD

# postfix expression: ABC/-AK/L-*
# postfix_expression:  *-A/BC-/AKL
