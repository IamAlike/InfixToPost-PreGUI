﻿
# Description: program converts infix to postfix notation



class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''

        for c in expr:
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()
                else:
                    while (not self.stack.is_empty()) and self.hasLessOrEqualPriority(c, self.stack.peek()):
                        output += self.stack.pop()
                    self.stack.push(c)

        while (not self.stack.is_empty()):
            output += self.stack.pop()
        return output

    '''
     1. Reverse expression string
     2. Replace open paren with close paren and vice versa
     3. Get Postfix and reverse it
    '''

    def toPrefix(self, expr):
        reverse_expr = ''
        for c in expr[::-1]:
            if c == '(':
                reverse_expr += ")"
            elif c == ')':
                reverse_expr += "("
            else:
                reverse_expr += c

        reverse_postfix = self.toPostfix(reverse_expr)

        return reverse_postfix[::-1]

    def convert(self, expr):
        try:
            result = eval(expr)
        except:
            result = expr

        return f'Original expr is: {expr} | Postfix is: {self.toPostfix(expr)} | Prefix is: {self.toPrefix(expr)} | Result is: {result}.'


if __name__ == "__main__":
    infix = InfixConverter()

