# Infix Expression Evaluator
# Uses modified ShuntingYard algorithm
class ExpressionEvaluator:
    @staticmethod
    def is_operator(c):
        return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'

    @staticmethod
    def determine_precedence(c):
        if c == '+' or c == '-':
            return 1
        if c == '*' or c == '/':
            return 2
        if c == '^':
            return 3
        return 0

    @staticmethod
    def calculate(a, b, operator):
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return a / b
        if operator == '^':
            return a ^ b

    @staticmethod
    def evaluate(expression):
        l = len(expression)
        operators = []
        operands = []
        index = 0
        while index < l:
            if expression[index] == '(':
                operators.append('(')
            elif expression[index].isdigit():
                value = 0
                while (index < l) and expression[index].isdigit():
                    value = (value * 10) + int(expression[index])
                    index += 1
                operands.append(value)
                index -= 1
            elif expression[index] == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    b = operands.pop()
                    a = operands.pop()
                    operator = operators.pop()
                    operands.append(expression.calculate(a, b, operator))
                operators.pop()
            else:
