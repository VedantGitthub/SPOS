import tkinter as tk
from tkinter import messagebox



def login():
    username = username_entry.get()
    password = password_entry.get()

    
    if not username or not password:
        messagebox.showwarning("Login Failed", "Please enter both username and password.")
    else:
        
        if username == "admin" and password == "password":  
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")



def cancel():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)




root = tk.Tk()
root.title("Login Window")
root.geometry("400x250")
root.configure(bg="#f0f5f9")
root.resizable(False, False)


title_label = tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg="#f0f5f9", fg="#333")
title_label.pack(pady=20)


tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=80)
username_entry = tk.Entry(root, width=30, font=("Arial", 10))
username_entry.place(x=150, y=80)


tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=120)
password_entry = tk.Entry(root, width=30, font=("Arial", 10), show="*")
password_entry.place(x=150, y=120)


login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
login_button.place(x=100, y=170)


cancel_button = tk.Button(root, text="Cancel", command=cancel, font=("Arial", 12), bg="#f44336", fg="white", width=10)
cancel_button.place(x=220, y=170)


root.mainloop()

