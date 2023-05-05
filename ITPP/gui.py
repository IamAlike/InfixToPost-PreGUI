from tkinter import *
from inpostprefix import *

root = Tk()

root.geometry("620x320")

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    infix = InfixConverter()
    es = infix.convert(inp)
    lbl.config(text=es)


# TextBox Creation
inputtxt = Text(root,
                height=5,
                width=20)

inputtxt.pack()

# Button Creation
printButton = Button(root,
                     text="Calculate",
                     command=printInput)
printButton.pack()
# exitButton = Button(root,
#                      text="goodbye",
#                      command=exit())
# exitButton.pack()

# Label Creation
lbl = Label(root, text="")
lbl.pack()
root.mainloop()

