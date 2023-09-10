from tkinter import Label
import tkinter
import tkinter as tk


from time import strftime
root = tk.Tk()
root.title("GUI")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(100, time)


label = Label(root, font=("ds=digital", 80),
              background="black", foreground="cyan")
label.pack(anchor='center')
time()
root.mainloop()
