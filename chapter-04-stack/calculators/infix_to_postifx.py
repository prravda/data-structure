def precedence(operator: str) -> int:
    if operator == '(' or operator == ')':
        return 0
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    return -1


def infix_to_postfix_calc(infix_expr: list[str]) -> list[str]:

    op = '+-*/'

    operators = []
    parsed_postfix = []

    for token in infix_expr:
        if token == '(':
            operators.append(token)

        elif token == ')':
            while operators:
                last = operators.pop()
                if last == '(':
                    break
                else:
                    parsed_postfix.append(last)

        elif token in op:
            while operators:
                last_op = operators[-1]
                if precedence(token) <= precedence(last_op):
                    parsed_postfix.append(operators.pop())
                else:
                    break
            operators.append(token)

        else:
            parsed_postfix.append(token)

    while operators:
        parsed_postfix.append(operators.pop())

    return parsed_postfix


def test():
    test_input_1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    test_output_1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
    assert infix_to_postfix_calc(test_input_1) == test_output_1
