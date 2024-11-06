import tkinter as tk
from tkinter import messagebox

def submit_form():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = country_listbox.get(tk.ACTIVE)
    agree = agree_var.get()
    if not first_name or not last_name or not email or not country or gender =="":
        messagebox.showwarning("Input Erro ","Please fill in all required field")
        return
    if not agree:
        messagebox.showwarning("Agreement Error ","Please agree to condition")
        return 
    messagebox.showinfo("Registration Successful", "Thank you for registering!")
    
    
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender_var.set("")
    country_listbox.selection_clear(0, tk.END)
    agree_var.set(0)


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")
root.configure(bg="#f0f5f9")


title_label = tk.Label(root, text="Student Registration Form", font=("Arial", 18, "bold"), bg="#f0f5f9", fg="#333")
title_label.pack(pady=10)


tk.Label(root, text="First Name:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=60)
first_name_entry = tk.Entry(root, width=30, font=("Arial", 10))
first_name_entry.place(x=200, y=60)


tk.Label(root, text="Last Name:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=100)
last_name_entry = tk.Entry(root, width=30, font=("Arial", 10))
last_name_entry.place(x=200, y=100)


tk.Label(root, text="Email:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=140)
email_entry = tk.Entry(root, width=30, font=("Arial", 10))
email_entry.place(x=200, y=140)


gender_var = tk.StringVar()
tk.Label(root, text="Gender:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=180)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#f0f5f9").place(x=200, y=180)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#f0f5f9").place(x=260, y=180)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", bg="#f0f5f9").place(x=330, y=180)


tk.Label(root, text="Country:", font=("Arial", 12), bg="#f0f5f9").place(x=50, y=220)
country_listbox = tk.Listbox(root, height=5, width=25, font=("Arial", 10), exportselection=False)
countries = ["United States", "Canada", "India", "United Kingdom", "Australia", "Germany", "France"]
for country in countries:
    country_listbox.insert(tk.END, country)
country_listbox.place(x=200, y=220)


agree_var = tk.IntVar()
agree_checkbutton = tk.Checkbutton(root, text="I agree to the terms and conditions", variable=agree_var, bg="#f0f5f9")
agree_checkbutton.place(x=50, y=340)


submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
submit_button.place(x=180, y=380)


root.mainloop()