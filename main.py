from tkinter import *


class BinaryExpressionTree:
    def __init__(self):
        self.stack = []


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all of window
        self.pack(fill=BOTH, expand=1)

        # create buttons
        calculateButton = Button(self, text="Calculate", command=self.calculate)
        calculateButton.place(x=20, y=260)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=100, y=260)

        # make labels
        expressionLabel = Label(self, text="Expression Field")
        expressionLabel.place(x=75, y=10)

        operandLabel = Label(self, text="Operands")
        operandLabel.place(x=20, y=90)

        operatorLabel = Label(self, text="Operators")
        operatorLabel.place(x=160, y=90)

        # make edit texts
        self.expressionEditText = Text(self, height=1, width=28)
        self.expressionEditText.place(x=25, y=40)

    def clickExitButton(self):
        exit()

    def calculate(self):
        exit()

    def appendExpField(self, s):
        self.expressionEditText += s


if __name__ == '__main__':
    # Create window
    root = Tk()
    app = Window(root)
    root.wm_title("Calculator")
    root.geometry("250x300")

    # Show window
    root.mainloop()
