from tkinter import *
import math as m

window = Tk()
window.title("Mari's Calculator")

e = Entry(window, width=25, borderwidth=10, font=("Helvetica", 15), fg="#ff0090")
e.grid(row=0, column=0, columnspan=4)


def button_click(key):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(key))


def button_cl():
    e.delete(0, END)


def button_add():
    first_num =e.get()
    global f_num
    global math
    math = "Add"
    f_num = float(first_num)
    e.delete(0,END)


def button_sub():
    first_num = e.get()
    global f_num
    global math
    math = "Subtract"
    f_num = float(first_num)
    e.delete(0, END)


def button_mult():
    first_num = e.get()
    global f_num
    global math
    math = "Multiply"
    f_num = float(first_num)
    e.delete(0, END)


def button_div():
    first_num = e.get()
    global f_num
    global math
    math = "Divide"
    f_num = float(first_num)
    e.delete(0, END)

'''
def button_mod():
    first_num = e.get()
    global f_num
    global math
    math = "Mod"
    f_num = float(first_num)
    e.delete(0, END)
'''

def button_exp():
    first_num = e.get()
    global f_num
    global math
    math = "Exp"
    f_num = float(first_num)
    e.delete(0, END)


def button_sqrt():
    first_num = e.get()
    global f_num
    global math
    math = "Sqrt"
    f_num = float(first_num)
    e.delete(0, END)


def button_eq():
    second_num = e.get()
    e.delete(0,END)
    if math == "Add":
        e.insert(0, f_num + float(second_num))
    if math == "Subtract":
        e.insert(0, f_num - float(second_num))
    if math == "Multiply":
        e.insert(0, f_num * float(second_num))
    if math == "Divide":
        if float(second_num) == 0:
            e.insert(0, "ERROR :(")
        else: e.insert(0, f_num / float(second_num))
    #if math == "Mod":
        #e.insert(0, f_num % float(second_num))
    if math == "Exp":
        e.insert(0, f_num ** float(second_num))
    if math == "Sqrt":
        e.insert(0, m.sqrt(f_num))


button_0 = Button(window, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_1 = Button(window, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_decpoint = Button(window, text=".", padx=31, pady=20, command=lambda: button_click("."))
button_addition = Button(window, text="+", padx=29, pady=20, command=button_add)
button_subtract = Button(window, text="-", padx=30, pady=20, command=button_sub)
button_multiply = Button(window, text="x", padx=29, pady=20, command=button_mult)
button_divide = Button(window, text="/", padx=30, pady=20, command=button_div)
#button_modulus = Button(window, text="%", padx=29, pady=20, command=button_mod)
button_exponential = Button(window, text="a^b", padx=23, pady=20, command=button_exp)
button_squareroot = Button(window, text="√", padx=23, pady=20, command=button_sqrt)
#button_clear = Button(window, text="CLEAR", padx=53, pady=20, bg="lightblue", command=button_cl)
button_clear = Button(window, text="CLEAR", padx=15, pady=20, bg="lightblue", command=button_cl)
button_equal = Button(window, text="ENTER", padx=54, pady=20, bg="lightgreen", command=button_eq)

button_0.grid(row=5, column=0)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_addition.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
#button_modulus.grid(row=1, column=2)
button_exponential.grid(row=1, column=1)
button_squareroot.grid(row=1, column=2)
button_clear.grid(row=1,column=0)
button_equal.grid(row=5, column=2, columnspan=3)
button_decpoint.grid(row=5, column=1)

window.mainloop()
