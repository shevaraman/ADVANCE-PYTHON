from tkinter import *

root = Tk()
root.title("BCA APP")
root.geometry("500x700")

f1 = Frame(root)
f1.config(bg="red")
f1.pack(fill=BOTH, expand=True)

l1 = Label(f1, text="ARITHMETIC OPERATION", bg="red", fg="yellow", font=("Arial", 25, "bold"))
l1.pack(pady=20)


f2 = Frame(root)
f2.config(bg="pink")
f2.pack(fill=BOTH, expand=True)

l2 = Label(f2, text="First Number:", bg="pink", fg="black", font=("Arial", 16))
l2.pack(pady=10)

root.mainloop()
