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
