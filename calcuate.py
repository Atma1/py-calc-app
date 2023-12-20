import tkinter as tk
from tkinter import ttk

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
    result_stack = Stack()
    operators = ['+', '-', '*', '/']

    for token in expression:
        if token.isdigit():
            result_stack.push(int(token))
        elif token in operators:
            operand2 = result_stack.pop()
            operand1 = result_stack.pop()

            if operand1 is None or operand2 is None:
                print("Error: Invalid expression")
                return None

            result = evaluate(operand1, operand2, token)

            result_stack.push(result)

    if not result_stack.is_empty():
        return result_stack.pop()
    else:
        print("Error: Invalid expression")
        return None

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    postfix_expression = []
    operator_stack = Stack()
    skip = 0

    for idx, token in enumerate(infix_expression):
        if skip > 0:
            skip -= 1
            pass
        elif token.isdigit():
            i = idx
            temp_number = 0
            skip = -1
            while (i < len(infix_expression)) and infix_expression[i].isdigit():
                temp_number = (temp_number * 10) + int(infix_expression[i])
                skip += 1
                i += 1
            postfix_expression.append(str(temp_number))
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
            operator_stack.pop()

    while not operator_stack.is_empty():
        postfix_expression.append(operator_stack.pop())

    return postfix_expression

# Stylish Calculator Class
class StylishCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator Infix Expression")
        self.geometry("400x500")

        # Styling
        self.style = ttk.Style(self)
        self.style.configure("TButton", padding=10, font=('Helvetica', 12))
        self.style.configure("TEntry", padding=10, font=('Helvetica', 14))

        # Create GUI elements
        self.entry = ttk.Entry(self, width=20, font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        # Number buttons
        for i in range(1, 10):
            ttk.Button(self, text=str(i), command=lambda i=i: self.on_button_click(i)).grid(row=(i-1)//3 + 1, column=(i-1)%3, sticky="nsew")

        # Operator buttons
        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            ttk.Button(self, text=operator, command=lambda operator=operator: self.on_operator_click(operator)).grid(row=i+1, column=3, sticky="nsew")

        # Other buttons
        ttk.Button(self, text='0', command=lambda: self.on_button_click(0)).grid(row=4, column=1, sticky="nsew")
        ttk.Button(self, text='=', command=self.on_calculate).grid(row=4, column=2, sticky="nsew")
        ttk.Button(self, text='C', command=self.on_clear).grid(row=4, column=0, sticky="nsew")
        ttk.Button(self, text='←', command=self.on_backspace).grid(row=4, column=3, sticky="nsew")

        # Configure grid
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_expression = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_expression + str(value))

    def on_operator_click(self, operator):
        current_expression = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_expression + operator)

    def on_clear(self):
        self.entry.delete(0, tk.END)

    def on_backspace(self):
        current_expression = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_expression[:-1])

    def on_calculate(self):
        infix_expression = self.entry.get()
        postfix_expression = infix_to_postfix(infix_expression)

        if postfix_expression:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, " ".join(postfix_expression))

            result = evaluate_postfix(postfix_expression)
            if result is not None:
                self.entry.insert(tk.END, "\n Hasil: " + str(result))

if __name__ == "__main__":
    app = StylishCalculator()
    app.mainloop()
