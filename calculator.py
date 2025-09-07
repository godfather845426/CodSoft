import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Smart GUI Calculator")
root.geometry("300x420")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

expression = ""

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except ZeroDivisionError:
        equation.set("Error: Div by 0")
        expression = ""
    except Exception:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation, font=('Arial', 20), bg="#2c2c2c", fg="white", bd=5, relief='sunken', justify='right')
display.grid(columnspan=4, ipadx=8, ipady=25, padx=10, pady=15)

buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('', 1, 2), ('', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in buttons:
    if text == '':
        continue  # skip blank cells
    if text == 'C':
        action = clear
    elif text == '=':
        action = equalpress
    elif text == '⌫':
        action = backspace
    else:
        action = lambda x=text: press(x)

    btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                    bg="#3e3e3e", fg="white", command=action)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()