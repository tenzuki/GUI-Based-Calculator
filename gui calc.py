
from tkinter import*


calc = Tk()
calc.title("parthiv calculator")
calc.minsize(width=364, height=523)
calc.maxsize(width=364, height=523)
#Code For Icon (Paste Here)

def displaybox(source, side):
    storeObj = Frame (source, borderwidth=4, bg="#566573")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, bg="black", fg="cyan", text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame. __init__(self)
        self.option_add('Font', 'Digital-7 Mono')
        self.option_add('size','500')
        self.pack(expand=YES, fill=BOTH)


        display = StringVar()
        Entry(self, relief=RIDGE,
                textvariable=display,justify='right',bd=26,fg="cyan",bg="black").pack(side=TOP, expand=YES,
                        fill=BOTH)

        for clearBut in(["CLEAR"],):
            erase = displaybox(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = displaybox(self, TOP)
            for char in NumBut:
                button(FunctionNum, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

        EqualsButton = displaybox(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                         lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,
                   lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))


    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("::Error::")

if __name__ == '__main__':
    app().mainloop()
