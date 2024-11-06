import tkinter as tk
from tkinter import messagebox

# Function to handle sign-up
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()

    # Check if all fields are filled and passwords match
    if not username or not password or not confirm_password or not email:
        messagebox.showwarning("Input Error", "Please fill in all fields!")
    elif password != confirm_password:
        messagebox.showwarning("Password Error", "Passwords do not match!")
    else:
        messagebox.showinfo("Sign-Up Successful", f"Welcome, {username}!")
        # Clear fields after sign-up
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Sign-Up Window")
root.geometry("400x400")

# Title label
title_label = tk.Label(root, text="Sign Up", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Username
tk.Label(root, text="Username:").pack(anchor="w", padx=20)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5, padx=20)

# Password
tk.Label(root, text="Password:").pack(anchor="w", padx=20)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5, padx=20)

# Confirm Password
tk.Label(root, text="Confirm Password:").pack(anchor="w", padx=20)
confirm_password_entry = tk.Entry(root, font=("Arial", 12), show="*")
confirm_password_entry.pack(pady=5, padx=20)

# Email
tk.Label(root, text="Email:").pack(anchor="w", padx=20)
email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.pack(pady=5, padx=20)

# Sign-Up Button
sign_up_button = tk.Button(root, text="Sign Up", font=("Arial", 14), bg="#4CAF50", fg="white", command=sign_up)
sign_up_button.pack(pady=20)

root.mainloop()
