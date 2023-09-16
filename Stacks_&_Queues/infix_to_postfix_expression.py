# https://www.codingninjas.com/studio/problems/day-23-:-infix-to-postfix-_1382146

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


def infixToPostfix(expr: str) -> str:
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


# infix_expression = "A*B-(C+D)+E"
t = int(input("Enter #testcases: "))
while t:
    infix_expression = input("Infix expression: ")
    postfix_expr = infixToPostfix(infix_expression)
    print('infix_expression: ', infix_expression)
    print('postfix_expression: ', postfix_expr)
    t -= 1
