from types import NoneType


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
def evaluate(op1, op2, token):
    if token == '+':
        result = op1 + op2
    elif token == '-':
        result = op1 - op2
    elif token == '*':
        result = op1 * op2
    elif token == '/':
        if op2 == 0:
            print("Error: Cannot divide by zero")
            return None
        result = op1 / op2

    return result

def evaluate_postfix(expression):
    """
    Evaluate an infix expression list.

    Args:
        expression: Infix expression list.

    Returns:
        Infix expression evaluated.
    
    """
    result_stack = Stack()
    operators = ['+', '-', '*', '/']

    for token in expression:
        if token.isdigit():
            result_stack.push(int(token))
        elif token in operators:
            operand2 = result_stack.pop()
            operand1 = result_stack.pop()

            if operand1 == None or operand2 == None:
                print("Error: Invalid expression")
                return None

            result = evaluate(operand1, operand2, token)

            result_stack.push(result)

    if not result_stack.is_empty():
        return result_stack.pop()
    else:
        print("Error: Invalid expression")
        return None

def infix_to_postfix(infix_expression: list) -> list:
    """
    Turns an infix expression e.g 3+4 into postfix expression e.g 34+.

    Args:
      infix_expression: A string of an infix expression.

    Returns:
      A list of postfix expression with each number/operand as seperate array.

    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    postfix_expression = []
    operator_stack = Stack()
    skip = 0

    for idx, token in enumerate(infix_expression):
        # Skip the current loop when the number is > 9.
        if skip > 0:
            skip -= 1
            pass
        # Check if the current string is a number
        elif token.isdigit():
            i = idx
            temp_number = 0
            skip = -1
            while (i < len(infix_expression)) and infix_expression[i].isdigit():
                temp_number = (temp_number * 10) + int(infix_expression[i])
                skip += 1
                i += 1
            postfix_expression.append(str(temp_number))
        # Check if the current string is an operand
        elif token in precedence:
            while (not operator_stack.is_empty() and
                   operator_stack.peek() in precedence and
                   precedence[operator_stack.peek()] >= precedence[token]):
                postfix_expression.append(operator_stack.pop())
            operator_stack.push(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while (not operator_stack.is_empty() and
                   operator_stack.peek() != '('):
                postfix_expression.append(operator_stack.pop())
            operator_stack.pop()  # Pop the '('

    while not operator_stack.is_empty():
        postfix_expression.append(operator_stack.pop())

    return postfix_expression

infix_expression = input("Enter an infix expression: ")

postfix_expression = infix_to_postfix(infix_expression)

print(postfix_expression)
if postfix_expression:
    print("Postfix expression:", " ".join(postfix_expression))

    result = evaluate_postfix(postfix_expression)
    if result is not None:
        print("Result:", result)