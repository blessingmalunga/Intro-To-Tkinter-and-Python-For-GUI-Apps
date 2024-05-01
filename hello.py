from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")

#formatting text on a label fg for formating text colour 
#bg or background fir formatting background colour 
# font(font family, size)
# height=() changing 

myVariable = Label(root,text="Hello world", fg="white", bg="red" , width=50, font=("Helvatica",30), height=2)
#pady(20) moving the label 20 pixels along the y axies
##padx(20) moving the label 20 pixels along the x axies
myVariable.pack(pady=10)


root.mainloop()