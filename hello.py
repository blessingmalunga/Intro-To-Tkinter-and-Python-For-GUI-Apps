from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")

#formatting text on a label fg for formating text colour 
#bg or background fir formatting background colour 
# font(font family, size)
# height=() changing 
# labels using grid
myVariable = Label(root,text="Simple Calculator", fg="white", bg="red" , width=15, font=("Helvatica",15))
#grid works with row= and column and they all  start at position 0
myVariable.grid(row=1,column=1,columnspan=3)

myVariable2 = Label(root,text="Addition")
#sticky can be used to position within the column N, W,E,S : S is South etc
myVariable2.grid(row=2,column=1,sticky=E)

myVariable3 = Label(root,text="Subtraction")
myVariable3.grid(row=3,column=1,sticky=W)
root.mainloop()