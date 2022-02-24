import tkinter as tk

root = tk.Tk()
root.title('Calculator')

e = tk.Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5) # columnspan passes in the number of columns comprised

Result = 0
last_op = None


class Buttons:
    def __init__(self, label, row, col, padx, pady, columnspan=1):
        self.label = label
        self.row = row
        self.col = col
        self.padx = padx
        self.pady = pady
        self.columnspan = columnspan

        b = tk.Button(root, text=self.label, padx=self.padx, pady=self.pady, command=self.click)
        b.grid(row=self.row, column=self.col, columnspan=self.columnspan)

        # b = tk.Button(root, text=self.label, padx=self.padx, pady=self.pady, command=lambda: self.click(a,b,c,...))
    # lambda is an anonymous func that returns the value at the right side of ':', in this ex the 'click()' function.
    # This way, in case that we need to call a functions that need parameters to be passed in ('command' only
    # accept func references, without the parameters needed) we would be able to pass in functions through lambda.

    def click(self):
        global e
        global Result   # we use global statement to affect the variable, otherwise it only affects the func environment
        global last_op
        if self.label in ('Clear', '+', '=', '-', '*', '/'):

            if self.label in ('+', '-', '*', '/') and last_op == '=':
                last_op = None
                e.delete(0, tk.END)
            if self.label in ('+', '-', '*', '/'):
                try:
                    Result += int(e.get())
                except ValueError:
                    pass
                finally:
                    e.delete(0, tk.END)
                    last_op = self.label

            elif self.label == '=':
                try:
                    Result = eval(str(Result) + last_op + e.get())
                    e.delete(0, tk.END)
                    e.insert(0, Result)
                    last_op = self.label
                except (TypeError, SyntaxError):
                    pass
            else:
                e.delete(0, tk.END)
                Result = 0
        else:
            if last_op == '=':
                e.delete(0, tk.END)
                last_op = None
                Result = 0
            current = str(e.get())
            e.delete(0, tk.END)
            e.insert(0, current+str(self.label))


b1 = Buttons(1, 3, 0, 20, 10)
b2 = Buttons(2, 3, 1, 20, 10)
b3 = Buttons(3, 3, 2, 20, 10)

b4 = Buttons(4, 2, 0, 20, 10)
b5 = Buttons(5, 2, 1, 20, 10)
b6 = Buttons(6, 2, 2, 20, 10)

b7 = Buttons(7, 1, 0, 20, 10)
b8 = Buttons(8, 1, 1, 20, 10)
b9 = Buttons(9, 1, 2, 20, 10)

b0 = Buttons(0, 4, 0, 20, 10)
b_c = Buttons('Clear', 4, 1, 37, 10, 2)

b_add = Buttons('+', 5, 0, 19, 10)
b_eq = Buttons('=', 5, 1, 47, 10, 2)

b_sb = Buttons('-', 6, 0, 20, 10)
b_mlt = Buttons('*', 6, 1, 21, 10)
b_div = Buttons('/', 6, 2, 20, 10)

root.mainloop()
