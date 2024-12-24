#4. Create a digital clock GUI application with Python.

import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  
    label.config(text=current_time)  
    label.after(1000, update_time)  

root = tk.Tk()
root.title("Digital Clock")

root.geometry("400x200")
root.config(bg="yellow")

label = tk.Label(root, font=("Arial", 40), fg="black", bg="yellow")
label.pack(expand=True)

update_time()

root.mainloop()
