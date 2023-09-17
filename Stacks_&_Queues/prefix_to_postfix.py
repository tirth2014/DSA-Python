"""
Long cumbersome Algorithm for Prefix to Postfix:
    1. Convert Prefix to Infix
    2. Convert Infix to Postfix


Algorithm for Prefix to Infix:

-> Read the Prefix expression in reverse order (from right to left)
-> If the symbol is an operand, then push it onto the Stack
-> If the symbol is an operator, then pop two operands from the Stack
-> Create a string by concatenating the two operands and the operator between them.
   string = (operand1 + operator + operand2)
   And push the resultant string back to Stack
-> Repeat the above steps until the end of Prefix expression.

At the end stack will have only 1 string i.e resultant string


Algorithm for Infix to Postfix:

Scan all the symbols one by one from left to right in the given Infix Expression.
-> If the symbol is an operand, then immediately append it to the Postfix Expression.
-> If the symbol is left parenthesis ‘( ‘, then Push it onto the Stack.
-> If the symbol is right parenthesis ‘)’, then Pop all the contents of the stack until the left parenthesis is popped
   and append each popped symbol to Postfix Expression.
-> If the symbol is an operator (+, –, *, /), then Push it onto the Stack.
   However, first, pop the operators which are already on the stack that have >= precedence than the current operator
   and append them to the postfix. If an open parenthesis '(' is there on stack_top then push the operator into the stack.
-> If the input is over, pop all the remaining symbols from the stack and append them to the postfix.
"""

from typing import List


def infixToPostfix(expr: str) -> str:

    def precedence(operator: str) -> int:
        # return precedence of operator
        if operator == '^':
            return 3
        elif operator in ['/', '*']:
            return 2
        elif operator in ['+', '-']:
            return 1
        else:
            return -1

    stk = []
    postfix_expr = ""

    for ch in expr:
        ch_prec = precedence(ch)
        # If a char. is operand, add it to output postfix string
        if ch.isalnum():
            postfix_expr += ch
        elif ch == '(':
            stk.append(ch)
        elif ch == ')':
            # pop from stack till '(' is encountered.
            while stk[-1] != '(':
                postfix_expr += stk.pop()
            stk.pop()
        elif stk and ch_prec > precedence(stk[-1]):
            stk.append(ch)
        else:
            while stk and precedence(stk[-1]) >= ch_prec:
                postfix_expr += stk.pop()
            stk.append(ch)

    while stk:
        postfix_expr += stk.pop()

    return postfix_expr


def prefixToInfix(prefix_expr: str) -> tuple:
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

    return infix_expr, infixToPostfix(infix_expr)



def prefixToPostfix(prefix_expr: str) -> tuple:
    return prefixToInfix(prefix_expr)


t = int(input("Enter #testcases: "))
while t:
    prefix_expression = input("\nprefix expression: ")
    infix, postfix_expression = prefixToPostfix(prefix_expression)
    print('infix_expression: ', infix)
    print('postfix_expression: ', postfix_expression)
    t -= 1

  
# Example:
# Enter #testcases: 2

# prefix expression: *+AB-CD
# infix_expression:  ((A+B)*(C-D))
# postfix_expression:  AB+CD-*

# prefix expression: *-A/BC-/AKL
# infix_expression:  ((A-(B/C))*((A/K)-L))
# postfix_expression:  ABC/-AK/L-*





"""
Simple Algorithm for Prefix to Postfix (Direct):

1. Read the Prefix expression in reverse order (from right to left)
2. If the symbol is an operand, then push it onto the Stack
3. If the symbol is an operator, then pop two operands from the Stack
4. Create a string by concatenating the two operands and the operator after them.
   string = operand1 + operand2 + operator
   And push the resultant string back to Stack
=> Repeat the above steps 1-4 until the end of the Prefix expression.
"""


def prefixToPostfix(prefix_expr: str) -> str:
    stack = []
    for ch in prefix_expr[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            # string = operand1 + operand2 + operator
            st = stack.pop() + stack.pop() + str(ch)
            stack.append(st)
    if stack:
        return stack.pop()


t = int(input("Enter #testcases: "))
while t:
    prefix_expression = input("\nprefix expression: ")
    postfix_expression = prefixToPostfix(prefix_expression)
    print('postfix_expression: ', postfix_expression)
    t -= 1
