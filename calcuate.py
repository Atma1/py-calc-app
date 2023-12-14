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
    stack = Stack()

    operators = set(['+', '-', '*', '/'])

    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()

            result = evaluate(operand1, operand2, token)

            stack.push(result)

    if not stack.is_empty():
        return stack.pop()
    else:
        print("Error: Invalid expression")
        return None

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    postfix_expression = []
    operator_stack = Stack()

    for token in infix_expression:
        print(token)
        if token.isdigit():
            postfix_expression.append(token)
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