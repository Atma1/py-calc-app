class PostfixExpressionEval:

    def eval_postfix(self, postfix):
        """
        Evaluates a postfix expression and returns the result as a string.

        Args:
           string  postfix: The postfix expression to evaluate.

        Returns:
            string: The result of the evaluation as a string.
        """

        stack = []
        for token in postfix.split():
            if token in "+-*/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = str(eval(f"{operand1}{token}{operand2}"))
                stack.append(result)
            else:
                stack.append(token)

        return stack.pop()