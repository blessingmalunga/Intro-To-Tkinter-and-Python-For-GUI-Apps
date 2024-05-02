
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Menu Program")

def new():
    pass
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


root.mainloop()