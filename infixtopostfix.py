class InfixToPostfix:

    def __init__(self):
        self.operators = {
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1,
            ")": 0,
        }

    def convert_to_postfix(self, infix_expression):
        """
        Convert infix expression to postfix expression.

        Args:
            str infix_expression: Infix expression. 

        Returns:
            str postfix_expression: Infix expression converted to postfix.
        """

        postfix_expression = []
        stack = []

        for token in infix_expression:
            if token.isalpha():
                postfix_expression.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack[-1] != "(":
                    postfix_expression.append(stack.pop())
                stack.pop()
            else:
                while stack and self.operators[token] <= self.operators[stack[-1]]:
                    postfix_expression.append(stack.pop())
                stack.append(token)

        while stack:
            postfix_expression.append(stack.pop())

        return "".join(postfix_expression)