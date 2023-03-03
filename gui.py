from tkinter import *
from matplotlib import pyplot as plt
from calculator import Calculator


class Custombox:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.c = Calculator()

        def calculate():
            self.c.exp = self.entry.get()  # storing data from entry box onto variable
            self.c.evaluate()
            a.change('Result is: {:.6f}'.format(self.c.op))

        def graph():
            self.c.exp = self.entry.get()
            self.c.graph()

        self.win = Toplevel()
        self.win.title(self.title)
        self.win.wm_attributes('-topmost', True)

        self.label = Label(self.win, text=self.text)
        self.label.grid(row=0, column=0, pady=(20, 10),
                        columnspan=3, sticky='w', padx=10)

        self.l = Label(self.win)

        self.entry = Entry(self.win, width=50)
        self.entry.grid(row=1, column=1, columnspan=3, padx=10)

        self.b1 = Button(self.win, text='Calculate',
                         width=10, command=calculate)
        self.b1.grid(row=3, column=1, pady=10)

        self.b2 = Button(self.win, text='Graph', width=10,
                         command=graph)
        self.b2.grid(row=3, column=2, pady=10)

        self.b3 = Button(self.win, text='Quit', width=10,
                         command=lambda: self.win.quit())
        self.b3.grid(row=3, column=3, pady=10)

    def __str__(self):
        return str(self.c.exp)

    def change(self, ran_text):
        self.l.config(text=ran_text, font=(0, 12))
        self.l.grid(row=2, column=1, columnspan=3, sticky='nsew', pady=5)


root = Tk()
root.withdraw()

a = Custombox(
    'Calculator', 'Enter an expression:')

root.mainloop()
