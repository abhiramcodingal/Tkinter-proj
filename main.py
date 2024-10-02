from tkinter import *

window = Tk()
window.title("Getting Started with widgets")
window.geometry("700x600")
window.configure(bg="aquamarine")

descreplbl = Label(window, text="Calculation app", width=20, font=("Lucida Sans", 15), bg="aquamarine4", fg="firebrick4")
descreplbl.pack()
lblenter1 = Label(window, text="Enter 1st number", width=15, font=("Monotype Corsiva", 13), bg="SeaGreen4", fg="gold3")
lblenter1.pack(pady=10)
num1ent = Entry(font=("Times New Roman", 10))
num1ent.pack(pady=3)
lblenter2 = Label(window, text="Enter 2nd number", width=15, font=("Monotype Corsiva", 13), bg="SeaGreen4", fg="gold3")
lblenter2.pack(pady=5)
num2ent = Entry(font=("Times New Roman", 10))
num2ent.pack(pady=5)
def multi():
    box1 = int(num1ent.get())
    box2 = int(num2ent.get())
    prod = box1 * box2
    show.delete(1.0, END)
    show.insert(END, f"The product is {prod}")
def div():
    box1 = int(num1ent.get())
    box2 = int(num2ent.get())
    quo = box1 // box2
    rem = box1 % box2
    show.delete(1.0, END)
    show.insert(END, f"The quotient is {quo}\n")
    show.insert(END, f"The remainder is {rem}")
def add():
    box1 = int(num1ent.get())
    box2 = int(num2ent.get())
    sum = box1 + box2
    show.delete(1.0, END)
    show.insert(END, f"The sum is {sum}")
def sub():
    box1 = int(num1ent.get())
    box2 = int(num2ent.get())
    diff = box1 - box2
    show.delete(1.0, END)
    show.insert(END, f"The difference is {diff}")

addbtn = Button(window, text=" + ", fg="SeaGreen3", bg="azure2", command=add, font=("Modern No. 20", 15), width=5)
addbtn.pack(pady=3)
subbtn = Button(window, text=" - ", fg="SeaGreen3", bg="azure2", command=sub, font=("Modern No. 20", 15), width=5)
subbtn.pack(padx=0.1)
mulbtn = Button(window, text=" X ", fg="SeaGreen3", bg="azure2", command=multi, font=("Modern No. 20", 15), width=5)
mulbtn.pack(padx=0.1)
divbtn = Button(window, text=" / ", fg="SeaGreen3", bg="azure2", command=div, font=("Modern No. 20", 15), width=5)
divbtn.pack(padx=0.1)
show = Text(font=("Franklin Gothic Demi Cond", 10), height=2, width=20)
show.pack(pady=7)

window.mainloop()