from tkinter import *
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, f"{expression} = {result}")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_square():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"{current}^2")
    try:
        result = eval(f"({current})**2")
        entry.delete(0, END)
        entry.insert(0, f"{current}^2 = {result}")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_square_root():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"sqrt({current})")
    try:
        result = math.sqrt(eval(current))
        entry.delete(0, END)
        entry.insert(0, f"sqrt({current}) = {result}")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_cube():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"{current}^3")
    try:
        result = eval(f"({current})**3")
        entry.delete(0, END)
        entry.insert(0, f"{current}^3 = {result}")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_cube_root():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"∛({current})")
    try:
        result = eval(f"({current})**(1/3)")
        entry.delete(0, END)
        entry.insert(0, f"∛({current}) = {result}")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_backspace():
    current = entry.get()
    entry.delete(len(current) - 1)

root = Tk()
root.title("Scientific Calculator")

entry = Entry(root, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=40)

button_1 = Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1),bg="lightblue")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2),bg="lightgreen")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3),bg="lightblue")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4),bg="lightgreen")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5),bg="lightblue")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6),bg="lightgreen")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7),bg="lightblue")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8),bg="lightgreen")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9),bg="lightblue")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0),bg="lightgreen")

button_decimal = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."),bg="lightblue")
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"),bg="lightgreen")
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"),bg="lightgreen")
button_multiply = Button(root, text="*", padx=44, pady=20, command=lambda: button_click("*"),bg="lightblue")
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"),bg="lightgreen")

button_equal = Button(root, text="=", padx=86, pady=20, command=button_equal,bg="lightblue")
button_clear = Button(root, text="Clear", padx=74, pady=20, command=button_clear,bg="lightblue")

button_square = Button(root, text="^2", padx=40, pady=20, command=button_square,bg="lightgreen")
button_square_root = Button(root, text="sqrt", padx=40, pady=20, command=button_square_root,bg="lightblue")
button_cube = Button(root, text="^3", padx=40, pady=20, command=button_cube,bg="lightgreen")
button_cube_root = Button(root, text="∛", padx=40, pady=20, command=button_cube_root,bg="lightblue")

button_backspace = Button(root, text="⌫", padx=40, pady=20, command=button_backspace,bg="lightblue")

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_decimal.grid(row=4, column=1)
button_clear.grid(row=6, column=0,columnspan=2)
button_add.grid(row=5, column=2)
button_equal.grid(row=5, column=0,columnspan=2)

button_subtract.grid(row=4, column=2)
button_multiply.grid(row=6, column=3)
button_divide.grid(row=6, column=2)

button_square.grid(row=1, column=3)
button_square_root.grid(row=2, column=3)
button_cube.grid(row=3, column=3)
button_cube_root.grid(row=4, column=3)

button_backspace.grid(row=5, column=3)

root.mainloop()
