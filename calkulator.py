from tkinter import *
import math
π =3.1415926535
e = 2.7182818284

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Calibri", 30, "bold"), bg="white", foreground="green",)  
        self.lbl.place(x=11, y=50)

        btns = ["1", "2", "3", "DEL","4", "5", "6", "C","7", "8", "9","=", "(", "0", ")","+", "-","*","/", "X^2","√","π","%","e"]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="black", fg = "white",
                   font=("Calibri", 30),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "%":
            self.formula = str((eval(self.formula))*0.01)
        elif operation == "√":
            self.formula = str((eval(self.formula))**0.5)  
       
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula, foreground = "green", background = "white")


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "white"
    root.geometry("485x635+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()