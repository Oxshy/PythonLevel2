from tkinter import *
from turtle import color
from time import strftime
root=Tk()
root.title("Akshay Digital clock")
root.geometry("400x400+300+200")
root.resizable(0,0)
label=Label(root,font=("Arial",16),text="The Time",bg="red",fg="black")
label.pack()
#label.place(x=50,y=50)
#label.grid(row=1,column=1)
def clock():
    tick=strftime("%H:%M:%S %p")
    label1.config(text=tick)
    label1.after(1000,clock)
label1=Label(root, font="Arial",bg="black",fg="red")
label1.pack()
clock()
root.mainloop()