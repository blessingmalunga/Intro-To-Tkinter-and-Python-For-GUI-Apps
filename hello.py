from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Entry Box")

def Clicked():
    global VLabel
    val = e.get()
    VLabel = Label(root,text="Your name is "+val )
    VLabel.pack()
#creating two functions to hide and show content
def hide():
    VLabel.pack_forget()

def show():
    VLabel.pack()


VLabel = Label(root,text="Please enter your name").pack()
e = Entry(root,width=30,fg="red",bg="white",font=("Arieal",20))
e.pack(pady=30)
fntBtn = Button(root,text="Enter Here.",command=Clicked).pack()

# create two  button to hide and show content 

hideBTN = Button(root,text="HIDE",command=hide).pack()
showBTN = Button(root,text="SHOW",command=show).pack()

root.mainloop()