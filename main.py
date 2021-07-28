from tkinter import *
from py_expression_eval import Parser


# GUI
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all of window
        self.pack(fill=BOTH, expand=1)

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

        # create buttons
        calculateButton = Button(self, text="Calculate", command=self.calculate)
        calculateButton.place(x=20, y=260)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=100, y=260)

        operand_index = 1
        # g = Grid().grid_location(x=50, y=260)
        for i in range(3):
            for j in range(3):
                Button(self, text=operand_index, command=self.appendExpField(str(operand_index)))\
                    .place(x=20 + j * 20, y=125 + i * 30)
                # b.grid(g, column=j, row=i)

                operand_index += 1


    @staticmethod
    def clickExitButton():
        exit()

    def calculate(self):
        exp = self.expressionEditText.get("1.0", "end-1c")
        self.expressionEditText.delete("1.0", "end-1c")
        try:
            answer = Parser().parse(exp).evaluate({})
            self.expressionEditText.insert(END, answer)

        except:
            self.expressionEditText.insert(END, 'SYNTAX ERROR')

    def appendExpField(self, s):
        self.expressionEditText.insert(END, s)


if __name__ == '__main__':
    # Create window
    root = Tk()
    app = Window(root)
    root.wm_title("Calculator")
    root.geometry("250x300")

    # Show window
    root.mainloop()
