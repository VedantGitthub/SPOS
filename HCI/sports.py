import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    contact = contact_entry.get()
    sport = sport_var.get()

    if not name or not contact or not sport:
        messagebox.showwarning("Input Error", "Please fill in all fields!")
    else:
        messagebox.showinfo("Registration Successful", f"Name: {name}\nContact: {contact}\nSport: {sport}")
        name_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        sport_var.set(None)

# Initialize the main window
root = tk.Tk()
root.title("Sports Academy Registration")
root.geometry("300x250")

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Contact
tk.Label(root, text="Contact Number:").pack(pady=5)
contact_entry = tk.Entry(root)
contact_entry.pack(pady=5)

# Preferred Sport
tk.Label(root, text="Preferred Sport:").pack(pady=5)
sport_var = tk.StringVar()

sport_list = ["Football", "Basketball", "Tennis"]
for sport in sport_list:
    tk.Radiobutton(root, text=sport, variable=sport_var, value=sport).pack(anchor="w")

# Submit Button
tk.Button(root, text="Register", command=submit_form).pack(pady=15)

root.mainloop()
