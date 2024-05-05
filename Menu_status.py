from tkinter import *

root = Tk()
root.title("Test Status Bar")
#root.geometry("400x400")
#root.config(background="white")

def class1():
   
    #main_frame.pack_forget()
    main_frame.pack()
    main_frame2.pack_forget()
    currentStatus.set("Class 1")

def class2():
    main_frame.pack_forget()
    #main_frame2.pack_forget()
    #main_frame2.pack_forget
    main_frame2.pack()
    currentStatus.set("Class 2")

welcomeLabel = Label(root,text="Welcome to Test Page",width=50,height=20,anchor=N)
welcomeLabel.pack()

main_frame = Frame(root,width=400, height=200,bg="red",bd=5,background="red")
main_frame2 = Frame(root,width=400, height=200,bd=5,background="green")

button1 = Button(root,text="Class 1",bg="blue",fg="red",width=10,anchor=N,command=class1)
button1.pack(padx=5)

button2 = Button(root,text="Class 2",bg="blue",fg="red",width=10,anchor=N,command=class2)
button2.pack()
currentStatus= StringVar()
statusBar = Label(root,textvariable =currentStatus,width=100,height=1,bd=2,relief="sunken",anchor=E)
statusBar.pack()
root.mainloop()