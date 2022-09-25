def postfix_calc(expr: list[str]) -> float:
    stack = []

    for token in expr:
        if token in "+-*/":
            val2 = stack.pop()
            val1 = stack.pop()

            # if a token is an operator -> evaluate
            if token == '+':
                stack.append(val1 + val2)
            if token == '-':
                stack.append(val1 - val2)
            if token == '*':
                stack.append(val1 * val2)
            if token == '/':
                stack.append(val1 / val2)

        # if a token is not an operator -> just append(push) into the stack
        else:
            stack.append(float(token))

    # return the evaluation result
    return stack.pop()


test_tokens = ['8', '2', '/', '3', '-', '3', '2', '*', '+']


def test_postfix_calculator():
    assert postfix_calc(test_tokens) == 7.0
