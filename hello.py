from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Entry Box")

def Clicked():
    val = e.get()
    VLabel = Label(root,text="Your name is "+val )
    VLabel.pack()


VLabel = Label(root,text="Please enter your name").pack()
e = Entry(root,width=30,fg="red",bg="white",font=("Arieal",20))
e.pack(pady=30)
fntBtn = Button(root,text="Enter Here.",command=Clicked).pack()

root.mainloop()