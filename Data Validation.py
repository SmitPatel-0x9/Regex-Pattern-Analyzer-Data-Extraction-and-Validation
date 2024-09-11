import re
import tkinter as tk
from tkinter import ttk

def validate_email():
    email = email_entry.get()
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        result_label.config(text="Valid email address", foreground="green")
    else:
        result_label.config(text="Invalid email address", foreground="red")

def validate_phone():
    phone = phone_entry.get()
    if re.match(r'^[0-9]{10}$', phone):
        result_label.config(text="Valid phone number", foreground="green")
    else:
        result_label.config(text="Invalid phone number", foreground="red")

def validate_password():
    password = password_entry.get()
    if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
        result_label.config(text="Valid password", foreground="green")
    else:
        result_label.config(text="Invalid password", foreground="red")

def show_password():
    password = password_entry.get()
    result_label.config(text=f"Password: {password}", foreground="black")

def clear_entries():
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black")

root = tk.Tk()
root.title("Web Form Data Validation")

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

email_button = ttk.Button(root, text="Validate Email", command=validate_email)
email_button.grid(row=0, column=2, padx=10, pady=5)

phone_label = ttk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

phone_entry = ttk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

phone_button = ttk.Button(root, text="Validate Phone", command=validate_phone)
phone_button.grid(row=1, column=2, padx=10, pady=5)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

password_button = ttk.Button(root, text="Validate Password", command=validate_password)
password_button.grid(row=2, column=2, padx=10, pady=5)

show_password_button = ttk.Button(root, text="Show Password", command=show_password)
show_password_button.grid(row=3, column=0, padx=10, pady=5)

clear_button = ttk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=3, column=1, padx=10, pady=5)

result_label = ttk.Label(root, text="", justify="center")
result_label.grid(row=4, columnspan=3, padx=10, pady=5)

root.mainloop()
