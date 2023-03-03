import math
from matplotlib import pyplot as plt


class Calculator:
    def __init__(self):
        self.l = []
        self.len = 0
        self.exp = ""
        self.op = 0

    def set_data(self):
        self.exp = input("Enter the expression to be evaluated: ")

    def sort_expression(self):
        self.exp = self.exp.replace("^", "**")
        self.exp = self.exp.replace("pi", "math.pi")
        self.exp = self.exp.replace("sin", "math.sin")
        self.exp = self.exp.replace("cos", "math.cos")
        self.exp = self.exp.replace("tan", "math.tan")

    def evaluate(self):
        # self.set_data()
        self.sort_expression()
        self.op = eval(self.exp)

    def numeric_evaluate(self):
        self.evaluate()
        print("Result is: {:.6f}".format(self.op))

    def graph(self):
        '''self.exp = input(
            "Enter expression to be graphed. Enter in terms of x: ")'''
        self.sort_expression()
        X = range(-50, 50)
        Y = [eval(self.exp) for x in X]
        plt.style.use("fivethirtyeight")
        plt.axhline(linewidth=2, color='#000000')
        plt.axvline(linewidth=2, color='#000000')
        plt.plot(X, Y)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("graph of y={}".format(self.exp))
        plt.tight_layout()
        plt.show()

    def parse_equation(self):
        nums = [0, 0, 0]
        accum = ''
        expo = False
        sign = 1
        for c in self.exp:
            if expo and c == '2':
                expo = False
                nums[0] = nums[1]
                nums[1] = 0
                accum = ''
            elif c in '1234567890.':
                accum += c
            elif c == 'x':
                nums[1] = float(accum) * sign
                accum = ''
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '^':
                expo = True
        nums[2] = float(accum) * sign
        return nums

    def quadratic(self):
        [a, b, c] = self.parse_equation()
        x1 = (-b+((b**2)-(4*a*c))**0.5)/(2*a)
        x2 = (-b-((b**2)-(4*a*c))**0.5)/(2*a)
        return x1, x2

