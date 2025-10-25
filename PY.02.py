from tkinter import *

root = Tk()  
root.title("NOTEPAD")
root.geometry("400x500")

l = Label(root, text="Username")  
l.pack()

e = Entry(root)
e.pack()

b = Button(root, text="Login") 
b.pack()

root.mainloop()
