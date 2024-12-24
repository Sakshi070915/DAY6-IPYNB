#3. Calculator

import tkinter as tk
from tkinter import ttk

def button_click(value):
    if value == "Clear":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry = ttk.Entry(root, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="ew")

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("0", 4, 0), ("Clear", 4, 1), ("=", 4, 2), ("/", 4, 3),
    (".", 5, 0), # Decimal on bottom-left
]

for (text, row, col) in buttons:
    action = lambda x=text: button_click(x)
    ttk.Button(root, text=text, command=action).grid(row=row, column=col, pady=5, padx=5, ipadx=10, ipady=10)

for col in range(1, 4):
    ttk.Label(root, text="").grid(row=5, column=col, padx=5, pady=5)

root.mainloop()
