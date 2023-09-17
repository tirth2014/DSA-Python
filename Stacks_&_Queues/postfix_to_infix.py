"""
Algorithm for Postfix to Infix:

1. Read the Postfix expression from left to right
2. If the symbol is an operand, then push it onto the Stack
3. If the symbol is an operator, then pop two operands from the Stack
4. Create a string by concatenating the two operands and the operator between them and parentheses on both sides.
   string = ( + operand2 + operator + operand1 + )
   And push the resultant string back to Stack
5. Repeat the above steps 1-4 until the end of the Postfix expression.
"""


def postfixToInfix(postfix: str) -> str:
    stack = []
    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            st = '(' + operand2 + str(ch) + operand1 + ')'
            stack.append(st)

    if stack:
        return stack.pop()


t = int(input("Enter #testcases: "))
while t:
    postfix_expression = input("\npostfix expression: ")
    infix_expression = postfixToInfix(postfix_expression)
    print('postfix_expression: ', infix_expression)
    t -= 1


# OUTPUT CONSOLE  
# Enter #testcases: 2

# postfix expression: AB+CD-*
# infix_expression:  ((A+B)*(C-D))

# postfix expression: ABC/-AK/L-*
# infix_expression:  ((A-(B/C))*((A/K)-L))
