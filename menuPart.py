
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Menu Program")

def new():
    my_label = Label(root,text="The item was clicked")
    my_label.pack()

def hide():
    my_frame.grid_forget()

def show():
    my_frame.grid(row=0,column=0)
#Defining the main  menu 

my_menu = Menu(root)
root.config(menu = my_menu)

#Creating sub menu 
sub_menu = Menu(my_menu)
#Adding names into  the sub menu  
my_menu.add_cascade(label="File",menu=sub_menu)
#Adding items in the sub menu
sub_menu.add_command(label="New",command=new)
sub_menu.add_separator()
#sub_menu.add_checkbutton()
sub_menu.add_command(label="Exit",command=root.quit)

hideBtn = Button(root,text="HIDE",command=hide)
hideBtn.grid(row=1,column=1)
showBtn = Button(root,text="SHOW",command=show)
showBtn.grid(row=1,column=2)
#Creating another sub menu Edit
edit_menu  = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy", command=new)
edit_menu.add_command(label="Cut", command=new)
edit_menu.add_command(label="Paste", command=new)


#adding frames to  the program 

my_frame = Frame(root,width=200,height=300,bg="blue",bd=5)
my_frame.grid(row=0,column=0)
myLabel = Label(my_frame,text="Hello",font=("Helvetica",20),fg="white")
myLabel.pack(padx=10,pady=10)

root.mainloop()