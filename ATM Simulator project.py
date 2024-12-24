#2. Create a simple console based ATM Simulator system.

import tkinter as tk
from tkinter import messagebox

users = {}

def create_account():
    username = entry_username.get()
    pin = entry_pin.get()
    
    if not username or not pin:
        messagebox.showerror("Error", "Username and PIN are required.")
        return
    
    if username in users:
        messagebox.showerror("Error", "Username already exists.")
        return
    
    users[username] = {"pin": pin, "balance": 0}
    messagebox.showinfo("Success", f"Account for {username} created successfully!")
    show_home_page()

def login(username):
    entered_username = entry_username.get()
    pin = entry_pin.get()
    
    if not entered_username or not pin:
        messagebox.showerror("Error", "Username and PIN are required.")
        return
    
    if entered_username not in users:
        messagebox.showerror("Error", "Username not found.")
        return
    
    if users[entered_username]["pin"] != pin:
        messagebox.showerror("Error", "Incorrect PIN.")
        return
    
    messagebox.showinfo("Success", f"Welcome {entered_username}!")
    show_atm_screen(entered_username)

def show_atm_screen(username):
    clear_window()
    
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    balance_label = tk.Label(
        main_frame, 
        text=f"Welcome {username}!\nBalance: ${users[username]['balance']:.2f}", 
        font=("Arial", 20),
        bg='white'
    )
    balance_label.pack(pady=10)

    amount_label = tk.Label(main_frame, text="Enter Amount:", font=("Arial", 14), bg='white')
    amount_label.pack(pady=5)
    
    instruction_label = tk.Label(
        main_frame, 
        text="(Click below to enter amount)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    instruction_label.pack(pady=(0,5))
    
    amount_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
    amount_entry.pack(pady=5)

    def withdraw():
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
            if amount > users[username]['balance']:
                messagebox.showerror("Error", "Insufficient balance.")
                return
            users[username]['balance'] -= amount
            balance_label.config(text=f"Welcome {username}!\nBalance: ${users[username]['balance']:.2f}")
            messagebox.showinfo("Success", f"Successfully withdrew ${amount:.2f}")
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def deposit():
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
            users[username]['balance'] += amount
            balance_label.config(text=f"Welcome {username}!\nBalance: ${users[username]['balance']:.2f}")
            messagebox.showinfo("Success", f"Successfully deposited ${amount:.2f}")
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    btn_withdraw = tk.Button(
        main_frame,
        text="Withdraw",
        font=("Arial", 12),
        command=withdraw,
        width=15,
        bg='#e1e1e1'
    )
    btn_withdraw.pack(pady=5)
    
    btn_deposit = tk.Button(
        main_frame,
        text="Deposit",
        font=("Arial", 12),
        command=deposit,
        width=15,
        bg='#e1e1e1'
    )
    btn_deposit.pack(pady=5)

    pin_label = tk.Label(main_frame, text="New PIN:", font=("Arial", 14), bg='white')
    pin_label.pack(pady=5)
    
    pin_instruction = tk.Label(
        main_frame, 
        text="(Click below to enter new PIN)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    pin_instruction.pack(pady=(0,5))
    
    new_pin_entry = tk.Entry(main_frame, font=("Arial", 14), show="*", width=20)
    new_pin_entry.pack(pady=5)

    def change_pin():
        new_pin = new_pin_entry.get()
        if not new_pin:
            messagebox.showerror("Error", "Please enter a new PIN.")
            return
        users[username]["pin"] = new_pin
        messagebox.showinfo("Success", "PIN changed successfully.")
        new_pin_entry.delete(0, tk.END)

    btn_change_pin = tk.Button(
        main_frame,
        text="Change PIN",
        font=("Arial", 12),
        command=change_pin,
        width=15,
        bg='#e1e1e1'
    )
    btn_change_pin.pack(pady=5)

    # Return to home button
    btn_home = tk.Button(
        main_frame,
        text="Return to Home",
        font=("Arial", 12),
        command=show_home_page,
        width=15,
        bg='#e1e1e1'
    )
    btn_home.pack(pady=20)

def show_home_page():
    clear_window()
    
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    title_label = tk.Label(
        main_frame,
        text="ATM Simulator",
        font=("Arial", 24, "bold"),
        bg='white'
    )
    title_label.pack(pady=(0, 20))
    
    if users:
        users_label = tk.Label(
            main_frame,
            text="Select Your Account",
            font=("Arial", 16),
            bg='white'
        )
        users_label.pack(pady=(0, 10))
        
        for user in users:
            btn_user = tk.Button(
                main_frame,
                text=user,
                font=("Arial", 12),
                command=lambda u=user: show_login_screen(u),
                width=20,
                bg='#e1e1e1'
            )
            btn_user.pack(pady=5)
    else:
        no_users_label = tk.Label(
            main_frame,
            text="No accounts available.\nPlease create a new account.",
            font=("Arial", 14),
            bg='white'
        )
        no_users_label.pack(pady=20)
    
    btn_create_account = tk.Button(
        main_frame,
        text="Create New Account",
        font=("Arial", 12),
        command=show_create_account_screen,
        width=20,
        bg='#e1e1e1'
    )
    btn_create_account.pack(pady=20)

def show_login_screen(username):
    clear_window()
    
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    title_label = tk.Label(
        main_frame,
        text="Login",
        font=("Arial", 24, "bold"),
        bg='white'
    )
    title_label.pack(pady=(0, 20))
    
    username_label = tk.Label(main_frame, text="Username", font=("Arial", 14), bg='white')
    username_label.pack(pady=5)
    
    username_instruction = tk.Label(
        main_frame, 
        text="(Pre-filled username)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    username_instruction.pack(pady=(0,5))
    
    global entry_username
    entry_username = tk.Entry(main_frame, font=("Arial", 14), width=20)
    entry_username.pack(pady=5)
    entry_username.insert(0, username)
    entry_username.config(state='readonly')
    
    pin_label = tk.Label(main_frame, text="PIN", font=("Arial", 14), bg='white')
    pin_label.pack(pady=5)
    
    pin_instruction = tk.Label(
        main_frame, 
        text="(Click below to enter PIN)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    pin_instruction.pack(pady=(0,5))
    
    global entry_pin
    entry_pin = tk.Entry(main_frame, font=("Arial", 14), show="*", width=20)
    entry_pin.pack(pady=5)

    btn_login = tk.Button(
        main_frame,
        text="Login",
        font=("Arial", 12),
        command=lambda: login(username),
        width=15,
        bg='#e1e1e1'
    )
    btn_login.pack(pady=5)
    
    btn_back = tk.Button(
        main_frame,
        text="Back to Home",
        font=("Arial", 12),
        command=show_home_page,
        width=15,
        bg='#e1e1e1'
    )
    btn_back.pack(pady=5)

def show_create_account_screen():
    clear_window()
    
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    title_label = tk.Label(
        main_frame,
        text="Create New Account",
        font=("Arial", 24, "bold"),
        bg='white'
    )
    title_label.pack(pady=(0, 20))
    
    username_label = tk.Label(main_frame, text="Choose a Username", font=("Arial", 14), bg='white')
    username_label.pack(pady=5)
    
    username_instruction = tk.Label(
        main_frame, 
        text="(Click below to enter username)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    username_instruction.pack(pady=(0,5))
    
    global entry_username
    entry_username = tk.Entry(main_frame, font=("Arial", 14), width=20)
    entry_username.pack(pady=5)
    
    pin_label = tk.Label(main_frame, text="Set a PIN", font=("Arial", 14), bg='white')
    pin_label.pack(pady=5)
    
    pin_instruction = tk.Label(
        main_frame, 
        text="(Click below to enter PIN)",
        font=("Arial", 10, "italic"),
        fg='blue',
        bg='white'
    )
    pin_instruction.pack(pady=(0,5))
    
    global entry_pin
    entry_pin = tk.Entry(main_frame, font=("Arial", 14), show="*", width=20)
    entry_pin.pack(pady=5)

    btn_create = tk.Button(
        main_frame,
        text="Create Account",
        font=("Arial", 12),
        command=create_account,
        width=15,
        bg='#e1e1e1'
    )
    btn_create.pack(pady=5)
    
    btn_back = tk.Button(
        main_frame,
        text="Back to Home",
        font=("Arial", 12),
        command=show_home_page,
        width=15,
        bg='#e1e1e1'
    )
    btn_back.pack(pady=5)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("ATM Simulator")
root.geometry("400x600")
root.configure(bg='white')

show_home_page()
root.mainloop()
