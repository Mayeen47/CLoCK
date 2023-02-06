from tkinter import *


from tkinter.ttk import *
from time import *
from datetime import datetime

cor = "#3d3d3d"
# creating window
root = Tk()
root.geometry("900x500")
root.title('\t\t\tDigital Clock  ')
root.configure(background=cor)


# Function to clock
def clock():
    time = datetime.now()
    string = time.strftime("%I:%M:%S %p")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    lbl.config(text=string)
    lbl.after(1000, clock)
    lb2.config(text=weekday + " : " + str(day) + " / " + str(month) + " / " + (year))


Label(root, font=("arial", 30), text="Digital Clock",
      foreground="white", background="green").pack()
lbl = Label(root, font=('DS-Digital', 80, 'bold'),
            background='black', foreground='white')
lbl.pack(anchor='center')


lb2 = Label(root, font=('arial', 60, 'bold'),
            background='gray', foreground='black')
lb2.pack(anchor='center')

# Call function to clock
clock()
root.mainloop()


