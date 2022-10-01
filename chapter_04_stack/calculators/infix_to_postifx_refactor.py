class FixParser:
    def __init__(self):
        self.add_and_sub = '+-'
        self.mul_and_div = '*/'
        self.brace_list = {')': '('}

    def precedence(self, op: str) -> int:
        if op in self.brace_list or op in self.brace_list.values():
            return 0
        if op in self.add_and_sub:
            return 1
        if op in self.mul_and_div:
            return 2
        return -1

    def infix_to_postfix(self, infix_expr: list[str]) -> list[str]:
        operator_list = []
        parsed_postfix = []

        for token in infix_expr:
            # case: open brace_list
            if token in self.brace_list.values():
                operator_list.append(token)
                continue

            # case: closed brace_list
            if token in self.brace_list:
                # iterate operator list with while loop
                while operator_list:
                    # till the last element is opened brace_list
                    # remove last element by pop() method
                    # from operator list
                    # and append it into parsed postfix
                    temp = operator_list.pop()
                    if temp in self.brace_list.values():
                        break
                    parsed_postfix.append(temp)
                continue

            # case: operator
            if token in self.add_and_sub or token in self.mul_and_div:
                # till the last element's precedence is larger than current token
                # remove the last element and append it into the parsed postfix list
                while operator_list:
                    last = operator_list[-1]
                    if self.precedence(last) >= self.precedence(token):
                        parsed_postfix.append(operator_list.pop())
                    else:
                        break

                operator_list.append(token)
                continue

            parsed_postfix.append(token)

        parsed_postfix.extend(operator_list)
        return parsed_postfix


def test():
    test_input_1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    test_output_1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
    assert FixParser().infix_to_postfix(test_input_1) == test_output_1