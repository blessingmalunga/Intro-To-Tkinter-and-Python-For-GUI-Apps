from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")

#Adding Clicked Function whic is handled by a button 
def Clicked():
    myBtn= Label(root,text="Welcome to Buttons creation").grid(row=4,column=0)

def clicked():
   myBtn= Label(root,text="Welcome to Buttons creation").grid(row=4,column=0) 

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

#Adding a button to our program // you can join pack or grid at the end of Button widget
myButton = Button(root,text="Pliz Click Me",command=Clicked).grid(row=3,column=3,sticky=S)

#adding button thats have a function with paramters using lamdba:
myButton2 = Button(root,text="Click to Display",command=clicked).grid(row=3,column=4)
root.mainloop()